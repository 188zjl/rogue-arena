FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    HOST=0.0.0.0 \
    PORT=18088 \
    DATA_DIR=/data

WORKDIR /app

RUN addgroup -S -g 10001 rogue \
    && adduser -S -D -H -u 10001 -G rogue rogue \
    && mkdir -p /data \
    && chown -R rogue:rogue /data /app

COPY --chown=rogue:rogue app.py manage_users.py windows2.html login.html admin.html DESIGN.md GAME_KNOWLEDGE.md ./
COPY --chown=rogue:rogue assets ./assets

USER rogue

EXPOSE 18088

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD wget -q -O - http://127.0.0.1:18088/health | grep -q '"status":"ok"' || exit 1

CMD ["python", "app.py"]
