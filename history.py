HISTORY_FACTS = {
    (1, 1):  "1999: The Euro was introduced, bringing 11 European economies under one currency.",
    (1, 15): "1929: Martin Luther King Jr. was born — a future leader of the civil rights movement.",
    (1, 26): "1950: India became a republic with its own constitution.",
    (1, 28): "1986: Space Shuttle Challenger broke apart shortly after launch, killing all 7 crew members.",

    (2, 4):  "2004: Mark Zuckerberg launched 'TheFacebook' from his Harvard dorm room.",
    (2, 11): "1990: Nelson Mandela walked free after 27 years in prison.",
    (2, 12): "1809: Charles Darwin was born — later changing science with his theory of evolution.",
    (2, 14): "1876: Alexander Graham Bell filed a patent for the telephone.",
    (2, 21): "1848: 'The Communist Manifesto' by Marx and Engels was published.",

    (3, 6):  "1899: Aspirin was patented — becoming one of the most used medicines ever.",
    (3, 14): "1879: Albert Einstein was born.",
    (3, 23): "1983: The US proposed the 'Star Wars' missile defense system.",

    (4, 4):  "1968: Martin Luther King Jr. was assassinated in Memphis.",
    (4, 12): "1961: Yuri Gagarin became the first human in space.",
    (4, 15): "1452: Leonardo da Vinci was born.",
    (4, 23): "1616: William Shakespeare passed away.",

    (5, 6):  "1954: Roger Bannister ran the first sub-4-minute mile.",
    (5, 25): "1977: Star Wars was released and changed cinema forever.",
    (5, 29): "1953: Hillary and Tenzing reached the summit of Mount Everest.",

    (6, 6):  "1944: D-Day — the largest seaborne invasion in history began.",
    (6, 16): "1963: Valentina Tereshkova became the first woman in space.",
    (6, 25): "1950: The Korean War began.",

    (7, 4):  "1776: The United States Declaration of Independence was adopted.",
    (7, 11): "1979: Skylab fell back to Earth after 6 years in orbit.",
    (7, 20): "1969: Neil Armstrong walked on the Moon.",

    (8, 6):  "1945: Hiroshima was hit by the first atomic bomb used in war.",
    (8, 9):  "1965: Singapore became an independent nation.",
    (8, 15): "1947: India gained independence from British rule.",
    (8, 25): "1989: Voyager 2 flew past Neptune.",

    (9, 2):  "1945: World War II officially ended.",
    (9, 11): "2001: The 9/11 attacks shook the world.",
    (9, 23): "1846: Neptune was discovered.",

    (10, 2):  "1869: Mahatma Gandhi was born.",
    (10, 4):  "1957: Sputnik 1, the first satellite, was launched.",
    (10, 14): "1947: Chuck Yeager broke the sound barrier.",
    (10, 28): "1886: The Statue of Liberty was unveiled.",

    (11, 9):  "1989: The Berlin Wall fell.",
    (11, 19): "1863: Lincoln delivered the Gettysburg Address.",

    (12, 1):  "1955: Rosa Parks sparked the civil rights movement.",
    (12, 10): "1948: The Universal Declaration of Human Rights was adopted.",
    (12, 17): "1903: The Wright Brothers achieved the first powered flight.",
    (12, 25): "800: Charlemagne was crowned emperor.",
    (12, 31): "1999: The world awaited the new millennium with Y2K fears.",
}

_FALLBACK = (
    "Every day writes history — some loudly, some quietly. "
    "Today might be the day you make yours."
)

def get_history(month: int, day: int) -> str:
    return HISTORY_FACTS.get((month, day), _FALLBACK)