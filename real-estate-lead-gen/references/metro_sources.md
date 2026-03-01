# Metro-Specific Lead Sources

Use this reference to adapt the discovery stage for different US metro areas.

## New York City

| Category | Primary Source | URL Pattern | Backup Source |
|----------|---------------|-------------|---------------|
| Price Reductions | StreetEasy | streeteasy.com/for-sale/{borough}/price_drop>50000 | Zillow price changes |
| FSBO | Zillow | zillow.com/new-york-ny/fsbo/ | Facebook Marketplace |
| Expired/Long DOM | StreetEasy | streeteasy.com/for-sale/nyc/status:off-market | Redfin |
| Pre-Foreclosure | PropertyShark | propertyshark.com/mason/Foreclosures/NYC | ACRIS |

**Boroughs:** Manhattan, Brooklyn, Queens, Bronx, Staten Island
**Key Neighborhoods:** Upper West Side, Upper East Side, Chelsea, Tribeca, West Village, Williamsburg, Park Slope, DUMBO, Astoria, Flushing

## Los Angeles

| Category | Primary Source | URL Pattern | Backup Source |
|----------|---------------|-------------|---------------|
| Price Reductions | Redfin | redfin.com/city/11203/CA/Los-Angeles/filter/price-reduced | Zillow |
| FSBO | Zillow | zillow.com/los-angeles-ca/fsbo/ | FSBO.com |
| Expired/Long DOM | Redfin | redfin.com/city/11203/CA/Los-Angeles/filter/status=off-market | Realtor.com |
| Pre-Foreclosure | Foreclosure.com | foreclosure.com/CA/Los-Angeles | County recorder |

**Regions:** West LA, Downtown, Hollywood, Silver Lake, Echo Park, Venice, Santa Monica, Pasadena, Glendale, Burbank

## Miami

| Category | Primary Source | URL Pattern | Backup Source |
|----------|---------------|-------------|---------------|
| Price Reductions | Zillow | zillow.com/miami-fl/price-reduced/ | Redfin |
| FSBO | Zillow | zillow.com/miami-fl/fsbo/ | FSBO.com |
| Expired/Long DOM | Redfin | redfin.com/city/11458/FL/Miami | Realtor.com |
| Pre-Foreclosure | Foreclosure.com | foreclosure.com/FL/Miami-Dade | County clerk |

**Regions:** Miami Beach, Brickell, Coral Gables, Coconut Grove, Wynwood, Edgewater, Downtown, Key Biscayne

## Chicago

| Category | Primary Source | URL Pattern | Backup Source |
|----------|---------------|-------------|---------------|
| Price Reductions | Redfin | redfin.com/city/29470/IL/Chicago/filter/price-reduced | Zillow |
| FSBO | Zillow | zillow.com/chicago-il/fsbo/ | FSBO.com |
| Expired/Long DOM | Redfin | redfin.com/city/29470/IL/Chicago | Realtor.com |
| Pre-Foreclosure | Foreclosure.com | foreclosure.com/IL/Cook | County recorder |

**Regions:** Lincoln Park, Lakeview, Gold Coast, River North, Wicker Park, Logan Square, Hyde Park, Bucktown

## San Francisco

| Category | Primary Source | URL Pattern | Backup Source |
|----------|---------------|-------------|---------------|
| Price Reductions | Redfin | redfin.com/city/17151/CA/San-Francisco/filter/price-reduced | Zillow |
| FSBO | Zillow | zillow.com/san-francisco-ca/fsbo/ | FSBO.com |
| Expired/Long DOM | Redfin | redfin.com/city/17151/CA/San-Francisco | Realtor.com |
| Pre-Foreclosure | Foreclosure.com | foreclosure.com/CA/San-Francisco | County recorder |

**Regions:** Pacific Heights, Marina, SoMa, Mission, Noe Valley, Castro, Hayes Valley, Russian Hill

## Generic (Any Metro)

For metros not listed above, use this default source mapping:

| Category | Primary Source | URL Pattern |
|----------|---------------|-------------|
| Price Reductions | Zillow | zillow.com/{city}-{state}/price-reduced/ |
| FSBO | Zillow | zillow.com/{city}-{state}/fsbo/ |
| Expired/Long DOM | Redfin | redfin.com/city/{id}/{state}/{city} |
| Pre-Foreclosure | Foreclosure.com | foreclosure.com/{state}/{county} |
