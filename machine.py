from fsm import TocMachine

def create_machine():
    machine = TocMachine(
        states=["user", "manual","show best game","game classify","state1", "state2","rpg","slg","casual","coorperation"],
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
                "dest": "show best game",
                "conditions": "is_going_to_show_bestgame",
            },
            {
                "trigger": "advance",
                "source": "manual",
                "dest": "game classify",
                "conditions": "is_going_to_game_classify",
            },
            {
                "trigger": "advance",
                "source": "game classify",
                "dest": "rpg",
                "conditions": "is_going_to_rpg",
            },
            {
                "trigger": "advance",
                "source": "game classify",
                "dest": "slg",
                "conditions": "is_going_to_slg",
            },
            {
                "trigger": "advance",
                "source": "game classify",
                "dest": "casual",
                "conditions": "is_going_to_casual",
            },
            {
                "trigger": "advance",
                "source": "game classify",
                "dest": "coorperation",
                "conditions": "is_going_to_coorperation",
            },
            {"trigger": "go_back", "source": ["state1", "state2","rpg"], "dest": "user"},
        ],
        initial="user",
        auto_transitions=False,
        show_conditions=True,
    )

    return machine