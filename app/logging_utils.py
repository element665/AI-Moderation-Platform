import json
import logging


def setup_logging():
    if logging.getLogger().handlers:
        return

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )


def get_logger(name: str):
    setup_logging()
    return logging.getLogger(name)


def log_event(logger, event: str, **fields):
    payload = {"event": event, **fields}
    logger.info(json.dumps(payload, sort_keys=True))
