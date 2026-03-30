"""
Tokenizer loading helpers for local model artifacts.
"""

import logging

from transformers import AutoTokenizer


_MISTRAL_REGEX_PATTERN = (
    r"[^\r\n\p{L}\p{N}]?[\p{Lu}\p{Lt}\p{Lm}\p{Lo}\p{M}]*[\p{Ll}\p{Lm}\p{Lo}\p{M}]+|"
    r"[^\r\n\p{L}\p{N}]?[\p{Lu}\p{Lt}\p{Lm}\p{Lo}\p{M}]+[\p{Ll}\p{Lm}\p{Lo}\p{M}]*|"
    r"\p{N}| ?[^\s\p{L}\p{N}]+[\r\n/]*|\s*[\r\n]+|\s+(?!\S)|\s+"
)
_MISTRAL_WARNING_FRAGMENT = "incorrect regex pattern"


class _SuppressMistralRegexWarning(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        return _MISTRAL_WARNING_FRAGMENT not in record.getMessage()


def _patch_mistral_regex(tokenizer):
    backend_tokenizer = getattr(tokenizer, "backend_tokenizer", None)
    if backend_tokenizer is None or getattr(tokenizer, "vocab_size", 0) <= 100000:
        return tokenizer

    try:
        import tokenizers
    except ImportError:
        return tokenizer

    split_pretokenizer = tokenizers.pre_tokenizers.Split(
        pattern=tokenizers.Regex(_MISTRAL_REGEX_PATTERN),
        behavior="isolated",
    )
    current_pretokenizer = backend_tokenizer.pre_tokenizer
    if isinstance(current_pretokenizer, tokenizers.pre_tokenizers.Sequence):
        current_pretokenizer[0] = split_pretokenizer
    else:
        if isinstance(current_pretokenizer, tokenizers.pre_tokenizers.Metaspace):
            current_pretokenizer = tokenizers.pre_tokenizers.ByteLevel(
                add_prefix_space=False,
                use_regex=False,
            )
        tokenizer.backend_tokenizer.pre_tokenizer = tokenizers.pre_tokenizers.Sequence(
            [split_pretokenizer, current_pretokenizer]
        )

    setattr(tokenizer, "fix_mistral_regex", True)
    return tokenizer


def load_tokenizer_with_compat(model_name_or_path: str, **kwargs):
    kwargs.setdefault("trust_remote_code", True)

    logger = logging.getLogger("transformers.tokenization_utils_tokenizers")
    warning_filter = _SuppressMistralRegexWarning()
    logger.addFilter(warning_filter)
    try:
        tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, **kwargs)
    finally:
        logger.removeFilter(warning_filter)

    return _patch_mistral_regex(tokenizer)