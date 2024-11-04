import json
import os
import sys
from pathlib import Path

from behavex_web.steps.web import *

# noinspection PyUnresolvedReferences
from features import env_manager


def before_all(context):
    """before_all behave hook"""
    load_environments_information(context)

    if context.config.userdata.get("env") is None:
        environment = "dev"
    else:
        environment = context.config.userdata.get("env").lower()

    for env in context.config_data["aureum_envs"]:
        if env["environment"] == environment:
            context.app_url = env["url"]
            context.api_url = env["api"]
            context.users = env['user_type']

    logging.info("{} APP URL: {} - API URL: {}".format("AUREUM", context.app_url, context.api_url))

    # Storing all variables in a context variable
    context.env_config = {
        "app_url": context.app_url,
        "api_url": context.api_url,
        "app_name": "Aureum",
        "environment": environment.upper(),
        "execution_tags": os.environ.get("TAGS", "").upper().split(";"),
        "company": "Aureum",
    }
    context.execution_summary_filename = os.path.abspath(
        os.path.join(os.environ.get("OUTPUT"), "..", "output", "execution_summary.txt")
    )


def before_feature(context, features):
    """before_feature behave hook"""
    for feature in features.scenarios:
        if "DEPRECATED" in feature.tags:
            feature.skip("This feature has been deprecated...")
        else:
            for tag in feature.tags:
                if "MUTE_" in tag:
                    feature.tags.append("MUTE")
                    break


def before_scenario(context, scenario):
    """before_scenario behave hook"""
    context.record_network_event_api_logs = True
    context.performance_logs = {}
    if "MUTE" in scenario.tags and "MUTE" not in context.env_config["execution_tags"]:
        scenario.skip("Avoid running muted scenario (it will be run in a separate test plan)")
        return

    context.performance_scenario = True if "PERFORMANCE" in scenario.tags else False
    print("------------------------------------------")
    print("Running Scenario: {}".format(scenario.name))
    print("------------------------------------------")


def before_step(context, step):
    """before_step behave hook"""
    context.step = step


def after_step(context, step):
    """after_step behave hook"""
    pass


def after_scenario(context, scenario):
    """after_scenario behave hook"""
    with open(context.execution_summary_filename, "a+") as f:
        if "MUTE" in scenario.tags and scenario.status == "failed":
            f.write("MUTED_SCENARIO: {}: {}\n".format(scenario.feature.name, scenario.name))
        if "MUTE" not in scenario.tags and scenario.status == "failed":
            failed_cause = ""
            for step_detail in scenario.steps:
                if step_detail.exception is not None:
                    failed_cause = step_detail.exception
            f.write("FAILING_SCENARIO: {}${}$ERROR: {}\n".format(scenario.feature.name, scenario.name, failed_cause))
        if scenario.status in ["passed", "failed"]:
            f.write("EXECUTED_SCENARIO: {}: {}\n".format(scenario.feature.name, scenario.name))
            print("------------------------------------------")
            print("Scenario Completed: {}".format(scenario.name))
            print("------------------------------------------")


def after_feature(context, feature):
    """after_feature behave hook"""
    pass


def after_all(context):
    """after_all behave hook"""
    pass


# ####################################################################################################
# ########################################## HELPER METHODS ##########################################
# ####################################################################################################

# noinspection PyBroadException
def load_environments_information(context):
    try:
        config_path = Path.cwd() / "config.json"
        with open(str(config_path)) as json_file:
            config_data = json.load(json_file)
        context.config_data = config_data
    except Exception:
        print("Please Contact Admin and ask for the config file")
        sys.exit(1)
