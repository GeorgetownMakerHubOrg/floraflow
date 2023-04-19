# GNU General Public License <https://www.gnu.org/licenses>
#
# Copyright (c) 2021 F. Pascal Girard
#

# Which pod am I?
POD = "pandora" # e.g. "matrix"

MQTT_PUB_TOPIC = "grow/"+POD+"/satellite/SENSOR"

FAILSAFE_TEMPERATURE = 100

ALERT_TOPIC = "grow/"+POD+"/alert"

QB96_COEFFICIENT = 0.0150538885266     # QB96 coefficient for calculating the Lux->PPFD
QB288_COEFFICIENT = 0.01549375         # QB288 coefficient for Lux->PPFD
COEFFICIENT = QB288_COEFFICIENT
LEAF_OFFSET = -4.5

INTERVAL = 1000       # Sampling in Ms for satellite


