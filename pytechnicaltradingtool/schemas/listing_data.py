from pydantic import BaseModel, Field


class ListingData(BaseModel):
    """This class simplifies creating Listing objects using data from outside sources where the field name doesn't
    match the model's field names.  The class is representative of data from
    https://www.nasdaq.com/market-activity/stocks/screener
    """

    name: str = Field(..., alias="Name")
    ticker: str = Field(..., alias="Symbol")
    country: str = Field(None, alias="Country")
    sector: str = Field(None, alias="Sector")
    industry: str = Field(None, alias="Industry")
