"""
Webhook & n8n / Zapier Exporter.
Enables one-click dispatch of researched dossiers and generated copy
to any external automation platform, CRM, or team channel.
"""
from typing import Dict, Any, Optional
import httpx

class WebhookExporter:
    def __init__(self, timeout: float = 10.0):
        self.timeout = timeout

    async def dispatch(self, webhook_url: str, payload: Dict[str, Any], headers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        """
        Dispatches payload to an external HTTP webhook (n8n, Zapier, Make, Slack).
        """
        req_headers = {"Content-Type": "application/json", "User-Agent": "ProspectPulse-Agent/1.2.0"}
        if headers:
            req_headers.update(headers)

        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                resp = await client.post(webhook_url, json=payload, headers=req_headers)
                return {
                    "success": resp.status_code < 400,
                    "status_code": resp.status_code,
                    "response_preview": resp.text[:200]
                }
        except Exception as e:
            return {
                "success": False,
                "status_code": 0,
                "error": str(e)
            }
