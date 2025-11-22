#!/bin/bash

# SeleniumサーバーURL
SELENIUM_URL="http://localhost:4444"

# 現在のセッション数を取得
CURRENT_SESSIONS=$(curl -sSL -X GET "$SELENIUM_URL/status" | jq '.value.nodes[0].slots | map(select(.session != null)) | length')

echo "Current Sessions: $CURRENT_SESSIONS"
echo "Max Sessions: $SE_NODE_MAX_SESSIONS"

# セッション数が最大値に達しているか確認
if [ "$CURRENT_SESSIONS" -ge "$SE_NODE_MAX_SESSIONS" ]; then
    echo "Session count ($CURRENT_SESSIONS) has reached the maximum limit ($SE_NODE_MAX_SESSIONS). Restarting container..."
    exit 1
else
    echo "Session count is under control."
    exit 0
fi
