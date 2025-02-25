from enum import Enum


class GridpointForecastPeriodTemperatureTrend(str, Enum):
    FALLING = "falling"
    RISING = "rising"
    NONE = ""

    def __str__(self) -> str:
        return str(self.value)
