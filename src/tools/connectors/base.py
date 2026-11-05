"""
Base Connector Interface for Lead Intelligence Sources.
Any new platform connector (LinkedIn, Crunchbase, Web, Twitter/X) inherits from this class.
"""
from abc import ABC, abstractmethod
from typing import Optional
from src.models.schema import NormalizedLeadSignal

class BaseConnector(ABC):
    @abstractmethod
    async def fetch_signal(self, target_identifier: str, **kwargs) -> Optional[NormalizedLeadSignal]:
        """
        Fetch raw data from the platform and normalize it into NormalizedLeadSignal.
        
        Args:
            target_identifier: A URL, domain, or handle (e.g. 'acme.com', 'linkedin.com/in/john')
        """
        pass
