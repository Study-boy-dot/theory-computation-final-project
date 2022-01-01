from fsm import TocMachine

def create_machine():
    machine = TocMachine(
        states=["user", "manual","show_bestgame","game_classify",
                    "rpg","slg","casual","coorperation","fsm"],
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
                "dest": "show_bestgame",
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
                "source": "manual",
                "dest": "fsm",
                "conditions": "is_going_to_fsm",
            },
            {
                "trigger": "advance",
                "source": "rpg",
                "dest": "rpg",
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
                "dest": "slg",
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
                "dest": "casual",
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
                "dest": "coorperation",
                "conditions": "is_going_to_briefly_coorperation",
            },
            {
                "trigger": "advance", 
                "source": ["show_bestgame","game_classify",
                    "rpg","slg","casual","coorperation","fsm"], 
                "dest":"manual",
                "conditions":"is_going_back_to_manual",
            },
        ],
        initial="user",
        auto_transitions=False,
        show_conditions=True,
    )

    return machine