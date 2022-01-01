from fsm import TocMachine

def create_machine():
    machine = TocMachine(
        states=["user", "manual","show_bestgame","game_classify",
                    "rpg","slg","casual","coorperation",
                    "briefly_bestgame","briefly_rpg",
                    "briefly_slg","briefly_casual",
                    "briefly_coorperation"],
        transitions=[
            {
                "trigger": "advance",
                "source": "user",
                "dest": "manual",
                "conditions": "is_going_to_manual",
            },
            {
                "trigger": "advance",
                "source": "manual",
                "dest": "show_bestgame",
                "conditions": "is_going_to_show_bestgame",
            },
            {
                "trigger": "advance",
                "source": "show_bestgame",
                "dest": "briefly_bestgame",
                "conditions": "is_going_to_briefly_bestgame",
            },
            {
                "trigger": "advance",
                "source": "manual",
                "dest": "game_classify",
                "conditions": "is_going_to_game_classify",
            },
            {
                "trigger": "advance",
                "source": "game_classify",
                "dest": "rpg",
                "conditions": "is_going_to_rpg",
            },
            {
                "trigger": "advance",
                "source": "rpg",
                "dest": "briefly_rpg",
                "conditions": "is_going_to_briefly_rpg",
            },
            {
                "trigger": "advance",
                "source": "game_classify",
                "dest": "slg",
                "conditions": "is_going_to_slg",
            },
            {
                "trigger": "advance",
                "source": "slg",
                "dest": "briefly_slg",
                "conditions": "is_going_to_briefly_slg",
            },
            {
                "trigger": "advance",
                "source": "game_classify",
                "dest": "casual",
                "conditions": "is_going_to_casual",
            },
            {
                "trigger": "advance",
                "source": "casual",
                "dest": "briefly_casual",
                "conditions": "is_going_to_briefly_casual",
            },
            {
                "trigger": "advance",
                "source": "game_classify",
                "dest": "coorperation",
                "conditions": "is_going_to_coorperation",
            },
            {
                "trigger": "advance",
                "source": "coorperation",
                "dest": "briefly_coorperation",
                "conditions": "is_going_to_briefly_coorperation",
            },
            {"trigger": "go_back", "source": "rpg", "dest": "user"},
            {"trigger": "go_back", "source": "briefly_bestgame", "dest": "show_bestgame"},
            {"trigger": "go_back", "source": ["briefly_rpg"], "dest": "rpg"},
            {"trigger": "go_back", "source": ["briefly_slg"], "dest": "slg"},
            {"trigger": "go_back", "source": ["briefly_casual"], "dest": "casual"},
            {"trigger": "go_back", "source": ["briefly_coorperation"], "dest": "coorperation"},
        ],
        initial="user",
        auto_transitions=False,
        show_conditions=True,
    )

    return machine