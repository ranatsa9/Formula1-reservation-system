import random
from datetime import datetime
from zoneinfo import ZoneInfo

import streamlit as st


# ============================================================
# PAGE SETUP
# ============================================================

st.set_page_config(
    page_title="F1 2026 Ticket Experience",
    page_icon="🏎️",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# CURRENT DATE
# Uses Saudi Arabia time
# ============================================================

TODAY = datetime.now(
    ZoneInfo("Asia/Riyadh")
).date()


# ============================================================
# HTML HELPER
# ============================================================

def render_html(html_code):
    st.html(html_code)


# ============================================================
# 2026 RACE DATABASE
#
# Prices and sold-out statuses are simulated.
# Race dates control automatic booking availability.
# ============================================================

races = {

    "Australian Grand Prix": {
        "Round": 1,
        "Country": "Australia",
        "Code": "AU",
        "Price": 420,
        "Location": "Albert Park, Melbourne",
        "Race Date": "2026-03-08",
        "Display Date": "06 - 08 Mar",
        "Inventory Status": "Available"
    },

    "Chinese Grand Prix": {
        "Round": 2,
        "Country": "China",
        "Code": "CN",
        "Price": 380,
        "Location": "Shanghai International Circuit",
        "Race Date": "2026-03-15",
        "Display Date": "13 - 15 Mar",
        "Inventory Status": "Available"
    },

    "Japanese Grand Prix": {
        "Round": 3,
        "Country": "Japan",
        "Code": "JP",
        "Price": 520,
        "Location": "Suzuka International Racing Course",
        "Race Date": "2026-03-29",
        "Display Date": "27 - 29 Mar",
        "Inventory Status": "Available"
    },

    "Miami Grand Prix": {
        "Round": 4,
        "Country": "United States",
        "Code": "US",
        "Price": 850,
        "Location": "Miami International Autodrome",
        "Race Date": "2026-05-03",
        "Display Date": "01 - 03 May",
        "Inventory Status": "Available"
    },

    "Canadian Grand Prix": {
        "Round": 5,
        "Country": "Canada",
        "Code": "CA",
        "Price": 620,
        "Location": "Circuit Gilles-Villeneuve, Montreal",
        "Race Date": "2026-05-24",
        "Display Date": "22 - 24 May",
        "Inventory Status": "Available"
    },

    "Monaco Grand Prix": {
        "Round": 6,
        "Country": "Monaco",
        "Code": "MC",
        "Price": 1200,
        "Location": "Circuit de Monaco",
        "Race Date": "2026-06-07",
        "Display Date": "05 - 07 Jun",
        "Inventory Status": "Available"
    },

    "Barcelona-Catalunya Grand Prix": {
        "Round": 7,
        "Country": "Spain",
        "Code": "ES",
        "Price": 400,
        "Location": "Circuit de Barcelona-Catalunya",
        "Race Date": "2026-06-14",
        "Display Date": "12 - 14 Jun",
        "Inventory Status": "Available"
    },

    "Austrian Grand Prix": {
        "Round": 8,
        "Country": "Austria",
        "Code": "AT",
        "Price": 550,
        "Location": "Red Bull Ring, Spielberg",
        "Race Date": "2026-06-28",
        "Display Date": "26 - 28 Jun",
        "Inventory Status": "Available"
    },

    "British Grand Prix": {
        "Round": 9,
        "Country": "Great Britain",
        "Code": "GB",
        "Price": 750,
        "Location": "Silverstone Circuit",
        "Race Date": "2026-07-05",
        "Display Date": "03 - 05 Jul",
        "Inventory Status": "Available"
    },

    "Belgian Grand Prix": {
        "Round": 10,
        "Country": "Belgium",
        "Code": "BE",
        "Price": 620,
        "Location": "Circuit de Spa-Francorchamps",
        "Race Date": "2026-07-19",
        "Display Date": "17 - 19 Jul",
        "Inventory Status": "Full"
    },

    "Hungarian Grand Prix": {
        "Round": 11,
        "Country": "Hungary",
        "Code": "HU",
        "Price": 480,
        "Location": "Hungaroring, Budapest",
        "Race Date": "2026-07-26",
        "Display Date": "24 - 26 Jul",
        "Inventory Status": "Available"
    },

    "Dutch Grand Prix": {
        "Round": 12,
        "Country": "Netherlands",
        "Code": "NL",
        "Price": 580,
        "Location": "Circuit Zandvoort",
        "Race Date": "2026-08-23",
        "Display Date": "21 - 23 Aug",
        "Inventory Status": "Available"
    },

    "Italian Grand Prix": {
        "Round": 13,
        "Country": "Italy",
        "Code": "IT",
        "Price": 650,
        "Location": "Autodromo Nazionale Monza",
        "Race Date": "2026-09-06",
        "Display Date": "04 - 06 Sep",
        "Inventory Status": "Available"
    },

    "Spanish Grand Prix - Madrid": {
        "Round": 14,
        "Country": "Spain",
        "Code": "ES",
        "Price": 695,
        "Location": "Madrid",
        "Race Date": "2026-09-13",
        "Display Date": "11 - 13 Sep",
        "Inventory Status": "Available"
    },

    "Azerbaijan Grand Prix": {
        "Round": 15,
        "Country": "Azerbaijan",
        "Code": "AZ",
        "Price": 450,
        "Location": "Baku City Circuit",
        "Race Date": "2026-09-26",
        "Display Date": "24 - 26 Sep",
        "Inventory Status": "Available"
    },

    "Singapore Grand Prix": {
        "Round": 16,
        "Country": "Singapore",
        "Code": "SG",
        "Price": 800,
        "Location": "Marina Bay Street Circuit",
        "Race Date": "2026-10-11",
        "Display Date": "09 - 11 Oct",
        "Inventory Status": "Full"
    },

    "United States Grand Prix": {
        "Round": 17,
        "Country": "United States",
        "Code": "US",
        "Price": 700,
        "Location": "Circuit of The Americas, Austin",
        "Race Date": "2026-10-25",
        "Display Date": "23 - 25 Oct",
        "Inventory Status": "Available"
    },

    "Mexico City Grand Prix": {
        "Round": 18,
        "Country": "Mexico",
        "Code": "MX",
        "Price": 500,
        "Location": "Autódromo Hermanos Rodríguez",
        "Race Date": "2026-11-01",
        "Display Date": "30 Oct - 01 Nov",
        "Inventory Status": "Available"
    },

    "São Paulo Grand Prix": {
        "Round": 19,
        "Country": "Brazil",
        "Code": "BR",
        "Price": 600,
        "Location": "Interlagos, São Paulo",
        "Race Date": "2026-11-08",
        "Display Date": "06 - 08 Nov",
        "Inventory Status": "Available"
    },

    "Las Vegas Grand Prix": {
        "Round": 20,
        "Country": "United States",
        "Code": "US",
        "Price": 900,
        "Location": "Las Vegas Strip Circuit",
        "Race Date": "2026-11-21",
        "Display Date": "19 - 21 Nov",
        "Inventory Status": "Available"
    },

    "Qatar Grand Prix": {
        "Round": 21,
        "Country": "Qatar",
        "Code": "QA",
        "Price": 700,
        "Location": "Lusail International Circuit",
        "Race Date": "2026-11-29",
        "Display Date": "27 - 29 Nov",
        "Inventory Status": "Available"
    },

    "Abu Dhabi Grand Prix": {
        "Round": 22,
        "Country": "Abu Dhabi",
        "Code": "AE",
        "Price": 850,
        "Location": "Yas Marina Circuit",
        "Race Date": "2026-12-06",
        "Display Date": "04 - 06 Dec",
        "Inventory Status": "Available"
    }
}


# ============================================================
# TICKET TIERS
# ============================================================

TICKET_TIERS = {

    "General Admission": {
        "Multiplier": 1.0,
        "Description": (
            "Flexible access and the full race-weekend atmosphere."
        ),
        "Icon": "🎫"
    },

    "Grandstand Premium": {
        "Multiplier": 1.5,
        "Description": (
            "Reserved seating with an enhanced view of the action."
        ),
        "Icon": "🏟️"
    },

    "Champions Club VIP": {
        "Multiplier": 2.5,
        "Description": (
            "Premium hospitality for a luxury race-weekend experience."
        ),
        "Icon": "🏆"
    }
}


VALID_MEMBERSHIP_CODES = [
    "F1CLUB2026",
    "POLEPOSITION",
    "VIPPASS"
]


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def parse_race_date(date_string):

    return datetime.strptime(
        date_string,
        "%Y-%m-%d"
    ).date()


def get_live_status(details):

    race_date = parse_race_date(
        details["Race Date"]
    )

    if TODAY > race_date:
        return "Completed"

    if details["Inventory Status"] == "Full":
        return "Full"

    return "Available"


def get_next_race(database):

    future_races = []

    for race_name, details in database.items():

        race_date = parse_race_date(
            details["Race Date"]
        )

        if race_date >= TODAY:

            future_races.append(
                (
                    race_date,
                    race_name,
                    details
                )
            )

    if len(future_races) == 0:
        return None

    future_races.sort(
        key=lambda race: race[0]
    )

    return future_races[0]


def calculate_total(
    race_name,
    quantity,
    ticket_type
):

    base_price = races[
        race_name
    ]["Price"]

    multiplier = TICKET_TIERS[
        ticket_type
    ]["Multiplier"]

    return (
        base_price
        * multiplier
        * quantity
    )


def apply_discount(amount):

    return amount * 0.85


def apply_tax(amount):

    return amount * 1.15


def create_reservation_id():

    return f"F1-{random.randint(100000, 999999)}"


def open_booking(
    race_name,
    details
):

    st.session_state["selected_race"] = race_name

    st.session_state["selected_details"] = details

    st.session_state["confirmed_booking"] = None

    st.session_state["page"] = "booking"

    st.rerun()


def return_to_schedule():

    st.session_state["page"] = "schedule"

    st.session_state["confirmed_booking"] = None

    st.rerun()


# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state["page"] = "schedule"


if "confirmed_booking" not in st.session_state:
    st.session_state["confirmed_booking"] = None


# ============================================================
# DARK F1 DESIGN
# Keeps the app dark even when Streamlit uses light mode
# ============================================================

st.html(
    """
    <style>

    /* ======================================================
       DESIGN VARIABLES
    ====================================================== */

    :root {
        --f1-red: #e10600;
        --page-bg: #080b10;
        --card-bg: #15181e;
        --card-bg-soft: #11141a;
        --main-text: #ffffff;
        --muted-text: #9ca0aa;
        --soft-text: #d0d2d7;
        --border: rgba(255, 255, 255, 0.10);
    }


    /* ======================================================
       PAGE BACKGROUND
    ====================================================== */

    html,
    body,
    [data-testid="stAppViewContainer"],
    .stApp {

        background:

            radial-gradient(
                circle at 92% 3%,
                rgba(225, 6, 0, 0.24),
                transparent 32%
            ),

            radial-gradient(
                circle at 8% 65%,
                rgba(225, 6, 0, 0.05),
                transparent 28%
            ),

            var(--page-bg) !important;

        color:
            var(--main-text) !important;
    }


    [data-testid="stAppViewContainer"] > .main {
        background: transparent !important;
    }


    .block-container {
        max-width: 1250px;
        padding-top: 1.2rem;
        padding-bottom: 4rem;
    }


    /* ======================================================
       STREAMLIT HEADER
    ====================================================== */

    header[data-testid="stHeader"] {
        background:
            rgba(8, 11, 16, 0.96) !important;

        border-bottom:
            1px solid
            rgba(255, 255, 255, 0.05) !important;
    }


    [data-testid="stToolbar"] {
        background:
            transparent !important;
    }


    [data-testid="stDecoration"] {
        background:
            var(--f1-red) !important;
    }


    header[data-testid="stHeader"] button,
    header[data-testid="stHeader"] svg {
        color:
            white !important;
    }


    /* ======================================================
       PAGE HEADER
    ====================================================== */

    .portfolio-header {
        padding:
            15px
            0
            28px
            0;
    }


    .brand {
        color:
            var(--f1-red);

        font-size:
            13px;

        font-weight:
            900;

        letter-spacing:
            3px;
    }


    .main-title {
        color:
            var(--main-text);

        font-size:
            54px;

        font-weight:
            900;

        line-height:
            1.05;

        margin-top:
            8px;
    }


    .main-subtitle {
        color:
            var(--muted-text);

        font-size:
            18px;

        line-height:
            1.6;

        margin-top:
            12px;

        max-width:
            720px;
    }


    /* ======================================================
       SEARCH BAR
    ====================================================== */

    div[data-testid="stTextInput"]
    div[data-baseweb="input"] {

        background:
            #11141a !important;

        border:
            1px solid
            rgba(255, 255, 255, 0.12) !important;

        border-radius:
            12px !important;
    }


    div[data-testid="stTextInput"] input {

        background:
            transparent !important;

        color:
            white !important;

        caret-color:
            var(--f1-red) !important;
    }


    div[data-testid="stTextInput"] input::placeholder {

        color:
            #777b85 !important;

        opacity:
            1 !important;
    }


    div[data-testid="stTextInput"]
    div[data-baseweb="input"]:focus-within {

        border:
            1px solid
            rgba(225, 6, 0, 0.80) !important;

        box-shadow:
            0 0 0 1px
            rgba(225, 6, 0, 0.20) !important;
    }


    /* ======================================================
       RADIO FILTERS
    ====================================================== */

    div[role="radiogroup"] label,
    div[role="radiogroup"] p {

        color:
            var(--muted-text) !important;
    }


    /* ======================================================
       COUNTRY BADGE
    ====================================================== */

    .country-badge {

        display:
            inline-flex;

        align-items:
            center;

        justify-content:
            center;


        min-width:
            34px;

        height:
            24px;

        padding:
            0 8px;


        background:
            rgba(225, 6, 0, 0.14);


        border:
            1px solid
            rgba(225, 6, 0, 0.38);


        border-radius:
            7px;


        color:
            #ff4742;


        font-size:
            11px;

        font-weight:
            900;

        letter-spacing:
            1px;


        margin-right:
            9px;


        vertical-align:
            middle;
    }


    /* ======================================================
       NEXT RACE CARD
    ====================================================== */

    .next-race-card {

        background:
            linear-gradient(
                135deg,
                #191c22,
                #11141a
            );


        border:
            1px solid
            var(--border);


        border-left:
            5px solid
            var(--f1-red);


        border-radius:
            24px;


        padding:
            34px;


        margin:
            15px
            0
            38px
            0;


        box-shadow:
            0 22px 65px
            rgba(0, 0, 0, 0.38);
    }


    .next-label {

        color:
            var(--f1-red);

        font-size:
            12px;

        font-weight:
            900;

        letter-spacing:
            2px;
    }


    .next-country {

        color:
            var(--main-text);

        font-size:
            40px;

        font-weight:
            900;

        margin-top:
            14px;


        display:
            flex;

        align-items:
            center;
    }


    .next-race-name {

        color:
            var(--muted-text);

        font-size:
            15px;

        text-transform:
            uppercase;

        margin-top:
            8px;
    }


    .next-date {

        color:
            var(--main-text);

        font-size:
            25px;

        font-weight:
            900;

        margin-top:
            22px;
    }


    .countdown {

        display:
            inline-block;


        background:
            linear-gradient(
                135deg,
                #e10600,
                #ff1b14
            );


        color:
            white;


        padding:
            9px
            15px;


        border-radius:
            999px;


        margin-top:
            18px;


        font-weight:
            900;


        box-shadow:
            0 8px 25px
            rgba(225, 6, 0, 0.24);
    }


    /* ======================================================
       RACE CARDS
    ====================================================== */

    .race-card {

        box-sizing:
            border-box;


        background:
            linear-gradient(
                145deg,
                #181b21,
                #101319
            );


        min-height:
            330px;


        padding:
            25px;


        border-radius:
            21px;


        border:
            1px solid
            var(--border);


        margin-bottom:
            10px;


        box-shadow:
            0 14px 38px
            rgba(0, 0, 0, 0.28);


        transition:
            transform 0.25s ease,
            border-color 0.25s ease,
            box-shadow 0.25s ease;
    }


    .race-card:hover {

        transform:
            translateY(-4px);


        border-color:
            rgba(225, 6, 0, 0.45);


        box-shadow:
            0 20px 50px
            rgba(0, 0, 0, 0.40);
    }


    .round-label {

        color:
            var(--muted-text);


        font-size:
            12px;

        letter-spacing:
            1.5px;

        font-weight:
            900;


        display:
            flex;

        align-items:
            center;
    }


    .country-name {

        color:
            var(--main-text);

        font-size:
            30px;

        font-weight:
            900;

        margin-top:
            16px;
    }


    .race-name {

        color:
            var(--muted-text);

        font-size:
            13px;

        text-transform:
            uppercase;

        min-height:
            35px;

        margin-top:
            4px;
    }


    .race-date {

        color:
            var(--f1-red);

        font-size:
            25px;

        font-weight:
            900;

        margin-top:
            17px;
    }


    .race-info {

        color:
            var(--soft-text);

        font-size:
            14px;

        margin-top:
            10px;
    }


    .status-available {

        color:
            #4ade80;

        font-weight:
            900;
    }


    .status-full {

        color:
            #f87171;

        font-weight:
            900;
    }


    .status-completed {

        color:
            #777b85;

        font-weight:
            900;
    }


    /* ======================================================
       BUTTONS
    ====================================================== */

    .stButton > button {

        background:
            #11141a !important;

        color:
            white !important;


        border:
            1px solid
            rgba(255, 255, 255, 0.18) !important;


        border-radius:
            999px !important;


        font-weight:
            800 !important;
    }


    .stButton > button:hover {

        border-color:
            var(--f1-red) !important;

        color:
            white !important;

        background:
            rgba(225, 6, 0, 0.12) !important;
    }


    .stButton > button[kind="primary"] {

        background:
            var(--f1-red) !important;

        border-color:
            var(--f1-red) !important;
    }


    .stButton > button:disabled {

        background:
            #11141a !important;

        color:
            #686b74 !important;

        border-color:
            rgba(255, 255, 255, 0.07) !important;
    }


    /* ======================================================
       SELECT BOX
    ====================================================== */

    div[data-testid="stSelectbox"]
    div[data-baseweb="select"] > div {

        background:
            #11141a !important;

        color:
            white !important;

        border-color:
            var(--border) !important;
    }


    /* ======================================================
       NUMBER INPUT
    ====================================================== */

    div[data-testid="stNumberInput"]
    div[data-baseweb="input"] {

        background:
            #11141a !important;

        border-color:
            var(--border) !important;
    }


    div[data-testid="stNumberInput"] input {

        color:
            white !important;
    }


    /* ======================================================
       BOOKING PAGE
    ====================================================== */

    .booking-hero {

        background:
            linear-gradient(
                135deg,
                #191c22,
                #11141a
            );


        border:
            1px solid
            var(--border);


        border-radius:
            24px;


        padding:
            32px;


        text-align:
            center;


        margin:
            18px
            0
            30px
            0;


        box-shadow:
            0 18px 50px
            rgba(0, 0, 0, 0.28);
    }


    .step-label {

        color:
            var(--f1-red);

        font-size:
            12px;

        font-weight:
            900;

        letter-spacing:
            2px;
    }


    .booking-code {

        display:
            inline-block;


        background:
            rgba(225, 6, 0, 0.14);


        border:
            1px solid
            rgba(225, 6, 0, 0.38);


        border-radius:
            7px;


        color:
            #ff4742;


        padding:
            5px
            9px;


        font-size:
            12px;

        font-weight:
            900;

        letter-spacing:
            1px;


        margin-bottom:
            10px;
    }


    .booking-title {

        color:
            var(--main-text);

        font-size:
            35px;

        font-weight:
            900;

        margin-top:
            10px;
    }


    .booking-meta {

        color:
            var(--muted-text);

        margin-top:
            10px;
    }


    /* ======================================================
       PAYMENT BOX
    ====================================================== */

    .payment-box {

        background:
            linear-gradient(
                145deg,
                #181b21,
                #101319
            );


        border:
            1px solid
            var(--border);


        border-radius:
            22px;


        padding:
            28px;


        margin:
            25px
            0;


        text-align:
            center;


        color:
            var(--main-text);
    }


    .payment-box h3 {

        color:
            var(--main-text);
    }


    .payment-box p {

        color:
            var(--soft-text);
    }


    .final-price {

        color:
            var(--main-text);


        font-size:
            38px;

        font-weight:
            900;


        margin:
            12px
            0;
    }


    /* ======================================================
       NATIVE STREAMLIT CONTAINERS
    ====================================================== */

    [data-testid="stVerticalBlockBorderWrapper"] {

        background:
            #11141a !important;

        border-color:
            var(--border) !important;
    }


    /* ======================================================
       NORMAL TEXT
    ====================================================== */

    h1,
    h2,
    h3,
    h4,
    p,
    label {

        color:
            var(--main-text);
    }


    /* ======================================================
       INFO / SUCCESS / WARNING BOXES
    ====================================================== */

    div[data-testid="stAlert"] {

        border-radius:
            14px !important;
    }


    /* ======================================================
       METRICS
    ====================================================== */

    [data-testid="stMetricValue"] {

        color:
            white !important;

        font-size:
            22px;
    }


    [data-testid="stMetricLabel"] {

        color:
            var(--muted-text) !important;

        font-size:
            13px;
    }


    /* ======================================================
       FOOTER
    ====================================================== */

    .disclaimer {

        color:
            #70747e;

        font-size:
            12px;

        line-height:
            1.8;

        text-align:
            center;

        margin-top:
            50px;
    }

    </style>
    """
)


# ============================================================
# SCHEDULE PAGE
# ============================================================

if st.session_state["page"] == "schedule":


    # --------------------------------------------------------
    # HEADER
    # --------------------------------------------------------

    render_html(
        """
        <div class="portfolio-header">

            <div class="brand">
                F1 2026 · PORTFOLIO PROJECT
            </div>

            <div class="main-title">
                Find your next race.
            </div>

            <div class="main-subtitle">
                Explore the 2026 season and experience
                an interactive Grand Prix reservation journey.
            </div>

        </div>
        """
    )


    # --------------------------------------------------------
    # NEXT RACE
    # --------------------------------------------------------

    next_race = get_next_race(
        races
    )


    if next_race is not None:

        next_date = next_race[0]

        next_name = next_race[1]

        next_details = next_race[2]


        days_left = (
            next_date - TODAY
        ).days


        if days_left == 0:

            countdown_text = "Race day"


        elif days_left == 1:

            countdown_text = "1 day to go"


        else:

            countdown_text = (
                f"{days_left} days to go"
            )


        render_html(
            f"""
            <div class="next-race-card">

                <div class="next-label">
                    UP NEXT · ROUND {next_details["Round"]}
                </div>

                <div class="next-country">

                    <span class="country-badge">
                        {next_details["Code"]}
                    </span>

                    {next_details["Country"]}

                </div>

                <div class="next-race-name">
                    {next_name}
                </div>

                <div class="next-date">
                    {next_details["Display Date"]}
                </div>

                <div class="race-info">
                    📍 {next_details["Location"]}
                </div>

                <div class="countdown">
                    🏁 {countdown_text}
                </div>

            </div>
            """
        )


    # --------------------------------------------------------
    # SEARCH AND FILTER
    # --------------------------------------------------------

    st.subheader(
        "Explore the season"
    )


    search_column, filter_column = (
        st.columns(
            [1.4, 1]
        )
    )


    with search_column:

        search_feature = (
            st.text_input(
                "Search",
                placeholder=(
                    "Search by race, country, or circuit..."
                ),
                label_visibility="collapsed"
            )
            .strip()
            .lower()
        )


    with filter_column:

        status_filter = st.radio(
            "Race filter",
            [
                "Upcoming",
                "Available",
                "Sold Out",
                "Completed",
                "All"
            ],
            horizontal=True,
            label_visibility="collapsed"
        )


    # --------------------------------------------------------
    # FILTER DATABASE
    # --------------------------------------------------------

    filtered_races = []


    for race_name, details in races.items():

        live_status = get_live_status(
            details
        )


        search_matches = (

            not search_feature

            or search_feature
            in race_name.lower()

            or search_feature
            in details["Country"].lower()

            or search_feature
            in details["Location"].lower()

        )


        if not search_matches:
            continue


        if (
            status_filter == "Upcoming"
            and live_status == "Completed"
        ):
            continue


        if (
            status_filter == "Available"
            and live_status != "Available"
        ):
            continue


        if (
            status_filter == "Sold Out"
            and live_status != "Full"
        ):
            continue


        if (
            status_filter == "Completed"
            and live_status != "Completed"
        ):
            continue


        filtered_races.append(
            (
                race_name,
                details,
                live_status
            )
        )


    # --------------------------------------------------------
    # NO RESULTS
    # --------------------------------------------------------

    if len(filtered_races) == 0:

        st.info(
            "No races match your search or selected filter."
        )


    # --------------------------------------------------------
    # RACE GRID
    # --------------------------------------------------------

    else:

        for i in range(
            0,
            len(filtered_races),
            2
        ):


            current_row = (
                filtered_races[
                    i:i + 2
                ]
            )


            if len(current_row) == 2:

                display_columns = st.columns(
                    2,
                    gap="large"
                )


            else:

                left_space, center_column, right_space = (
                    st.columns(
                        [1, 2, 1]
                    )
                )

                display_columns = [
                    center_column
                ]


            for column, race_data in zip(
                display_columns,
                current_row
            ):


                race_name = race_data[0]

                details = race_data[1]

                live_status = race_data[2]


                if live_status == "Available":

                    status_class = (
                        "status-available"
                    )

                    status_text = (
                        "AVAILABLE TO BOOK"
                    )


                elif live_status == "Full":

                    status_class = (
                        "status-full"
                    )

                    status_text = (
                        "SOLD OUT"
                    )


                else:

                    status_class = (
                        "status-completed"
                    )

                    status_text = (
                        "RACE COMPLETED"
                    )


                with column:

                    render_html(
                        f"""
                        <div class="race-card">

                            <div class="round-label">

                                <span class="country-badge">
                                    {details["Code"]}
                                </span>

                                ROUND {details["Round"]}

                            </div>

                            <div class="country-name">
                                {details["Country"]}
                            </div>

                            <div class="race-name">
                                {race_name}
                            </div>

                            <div class="race-date">
                                {details["Display Date"]}
                            </div>

                            <div class="race-info">
                                📍 {details["Location"]}
                            </div>

                            <div class="race-info">
                                💰 Demo price from
                                {details["Price"]:,} SAR
                            </div>

                            <div class="race-info">

                                Status:

                                <span class="{status_class}">
                                    {status_text}
                                </span>

                            </div>

                        </div>
                        """
                    )


                    if live_status == "Available":

                        if st.button(
                            "Reserve this race →",
                            key=(
                                f"reserve_{race_name}"
                            ),
                            use_container_width=True
                        ):

                            open_booking(
                                race_name,
                                details
                            )


                    elif live_status == "Full":

                        st.button(
                            "Sold out",
                            key=(
                                f"full_{race_name}"
                            ),
                            disabled=True,
                            use_container_width=True
                        )


                    else:

                        st.button(
                            "Race completed",
                            key=(
                                f"completed_{race_name}"
                            ),
                            disabled=True,
                            use_container_width=True
                        )


# ============================================================
# BOOKING PAGE
# ============================================================

elif st.session_state["page"] == "booking":


    selected_race = (
        st.session_state[
            "selected_race"
        ]
    )


    selected_details = (
        st.session_state[
            "selected_details"
        ]
    )


    selected_status = get_live_status(
        selected_details
    )


    # --------------------------------------------------------
    # SAFETY CHECK
    # --------------------------------------------------------

    if selected_status != "Available":

        st.error(
            "Booking for this race is no longer available."
        )


        if st.button(
            "← Back to schedule"
        ):

            return_to_schedule()


    else:


        # ----------------------------------------------------
        # BACK BUTTON
        # ----------------------------------------------------

        if st.button(
            "← Back to schedule"
        ):

            return_to_schedule()


        # ----------------------------------------------------
        # BOOKING HERO
        # ----------------------------------------------------

        render_html(
            f"""
            <div class="booking-hero">

                <div class="step-label">
                    BOOKING · ROUND
                    {selected_details["Round"]}
                </div>

                <div class="booking-code">
                    {selected_details["Code"]}
                </div>

                <div class="booking-title">
                    {selected_race}
                </div>

                <div class="booking-meta">
                    {selected_details["Display Date"]}
                    ·
                    {selected_details["Location"]}
                </div>

            </div>
            """
        )


        # ----------------------------------------------------
        # STEP 1
        # ----------------------------------------------------

        st.subheader(
            "1 · Choose your tickets"
        )


        quantity = st.number_input(
            "Number of tickets",
            min_value=1,
            max_value=10,
            value=1
        )


        # ----------------------------------------------------
        # STEP 2
        # ----------------------------------------------------

        st.subheader(
            "2 · Choose your experience"
        )


        selected_tier = st.selectbox(
            "Ticket tier",
            options=list(
                TICKET_TIERS.keys()
            )
        )


        tier_details = (
            TICKET_TIERS[
                selected_tier
            ]
        )


        tier_price = (
            selected_details["Price"]
            * tier_details["Multiplier"]
        )


        st.info(
            f"""
{tier_details["Icon"]} **{selected_tier}**

{tier_details["Description"]}

Demo price per ticket: **{tier_price:,.2f} SAR**
            """
        )


        # ----------------------------------------------------
        # STEP 3
        # ----------------------------------------------------

        st.subheader(
            "3 · Membership & offers"
        )


        user_code = (
            st.text_input(
                "Promo code",
                placeholder=(
                    "Try F1CLUB2026"
                )
            )
            .strip()
            .upper()
        )


        order_subtotal = calculate_total(
            selected_race,
            quantity,
            selected_tier
        )


        if (
            user_code
            in VALID_MEMBERSHIP_CODES
        ):

            discounted_total = (
                apply_discount(
                    order_subtotal
                )
            )

            discount_status = (
                "15% member discount"
            )


            if user_code:

                st.success(
                    "Membership verified. "
                    "15% discount applied."
                )


        else:

            discounted_total = (
                order_subtotal
            )

            discount_status = (
                "No discount"
            )


            if user_code:

                st.warning(
                    "Promo code not recognised."
                )


        final_total = apply_tax(
            discounted_total
        )


        # ----------------------------------------------------
        # STEP 4
        # ----------------------------------------------------

        st.subheader(
            "4 · Review your booking"
        )


        with st.container(
            border=True
        ):

            review_col1, review_col2 = (
                st.columns(2)
            )


            with review_col1:

                st.write(
                    f"**Race:** "
                    f"{selected_race}"
                )

                st.write(
                    f"**Experience:** "
                    f"{selected_tier}"
                )

                st.write(
                    f"**Quantity:** "
                    f"{quantity}"
                )


            with review_col2:

                st.write(
                    f"**Price per ticket:** "
                    f"{tier_price:,.2f} SAR"
                )

                st.write(
                    f"**Discount:** "
                    f"{discount_status}"
                )

                st.write(
                    "**VAT:** 15%"
                )


        # ----------------------------------------------------
        # PAYMENT BOX
        # ----------------------------------------------------

        render_html(
            f"""
            <div class="payment-box">

                <h3>
                    Final payment
                </h3>

                <p>
                    Subtotal:
                    <b>
                        {order_subtotal:,.2f} SAR
                    </b>
                </p>

                <p>
                    After discount:
                    <b>
                        {discounted_total:,.2f} SAR
                    </b>
                </p>

                <div class="final-price">
                    {final_total:,.2f} SAR
                </div>

                <p>
                    Including 15% VAT
                </p>

            </div>
            """
        )


        # ----------------------------------------------------
        # CONFIRM
        # ----------------------------------------------------

        if st.button(
            "Confirm reservation",
            type="primary",
            use_container_width=True
        ):


            st.session_state[
                "confirmed_booking"
            ] = {

                "Reservation ID": (
                    create_reservation_id()
                ),

                "Race": selected_race,

                "Code": (
                    selected_details[
                        "Code"
                    ]
                ),

                "Round": (
                    selected_details[
                        "Round"
                    ]
                ),

                "Location": (
                    selected_details[
                        "Location"
                    ]
                ),

                "Weekend": (
                    selected_details[
                        "Display Date"
                    ]
                ),

                "Tier": selected_tier,

                "Quantity": quantity,

                "Subtotal": order_subtotal,

                "Discount Status": (
                    discount_status
                ),

                "After Discount": (
                    discounted_total
                ),

                "Final Total": (
                    final_total
                )
            }


            st.rerun()


        # ----------------------------------------------------
        # RECEIPT
        # ----------------------------------------------------

        if (
            st.session_state[
                "confirmed_booking"
            ]
            is not None
        ):

            booking = (
                st.session_state[
                    "confirmed_booking"
                ]
            )


            st.success(
                "Reservation confirmed successfully!"
            )


            st.subheader(
                "Your ticket"
            )


            with st.container(
                border=True
            ):


                st.caption(
                    f"RESERVATION "
                    f"{booking['Reservation ID']}"
                )


                st.markdown(
                    f"## "
                    f"{booking['Code']} · "
                    f"{booking['Race']}"
                )


                st.caption(
                    "F1-inspired demo reservation"
                )


                receipt_col1, receipt_col2 = (
                    st.columns(2)
                )


                with receipt_col1:

                    st.write(
                        f"**Location:** "
                        f"{booking['Location']}"
                    )

                    st.write(
                        f"**Tickets:** "
                        f"{booking['Quantity']}"
                    )

                    st.write(
                        f"**Experience:** "
                        f"{booking['Tier']}"
                    )


                with receipt_col2:

                    st.write(
                        f"**Race weekend:** "
                        f"{booking['Weekend']}"
                    )

                    st.write(
                        f"**Round:** "
                        f"{booking['Round']}"
                    )

                    st.write(
                        "**Status:** Confirmed"
                    )


                st.divider()


                metric1, metric2, metric3 = (
                    st.columns(3)
                )


                metric1.metric(
                    "Subtotal",
                    (
                        f"{booking['Subtotal']:,.2f} "
                        f"SAR"
                    )
                )


                metric2.metric(
                    "After discount",
                    (
                        f"{booking['After Discount']:,.2f} "
                        f"SAR"
                    )
                )


                metric3.metric(
                    "Final total",
                    (
                        f"{booking['Final Total']:,.2f} "
                        f"SAR"
                    )
                )


                st.caption(
                    "Thank you for booking. "
                    "See you at the track."
                )


            receipt_text = f"""
F1-INSPIRED RESERVATION RECEIPT

Reservation ID: {booking["Reservation ID"]}

Race: {booking["Race"]}
Country Code: {booking["Code"]}
Round: {booking["Round"]}
Location: {booking["Location"]}
Race Weekend: {booking["Weekend"]}

Ticket Tier: {booking["Tier"]}
Quantity: {booking["Quantity"]}

Subtotal: {booking["Subtotal"]:,.2f} SAR
Discount: {booking["Discount Status"]}
After Discount: {booking["After Discount"]:,.2f} SAR
VAT: 15%
Final Total: {booking["Final Total"]:,.2f} SAR

Status: Confirmed

Portfolio demonstration only.
Not affiliated with Formula 1.
"""


            st.download_button(
                label="Download receipt",
                data=receipt_text,
                file_name=(
                    f"{booking['Reservation ID']}"
                    f"_receipt.txt"
                ),
                mime="text/plain",
                use_container_width=True
            )


# ============================================================
# FOOTER
# ============================================================

render_html(
    """
    <div class="disclaimer">

        Portfolio demonstration only.<br>

        Race dates are used to demonstrate
        automatic booking availability.<br>

        Prices, inventory and booking features
        are simulated.<br>

        This project is not affiliated with Formula 1.

    </div>
    """
)
