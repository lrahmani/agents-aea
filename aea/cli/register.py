# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2018-2019 Fetch.AI Limited
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""Implementation of the 'aea login' subcommand."""

import click

from aea.cli.registry.registration import register as register_new_account


def do_register(
    username: str, email: str, password: str, password_confirmation: str
) -> None:
    """
    Register a new Registry account.

    :param username: str username.
    :param email: str email.
    :param password: str password.
    :param password_confirmation: str password confirmation.

    :return: None
    """
    register_new_account(username, email, password, password_confirmation)
    click.echo("User successfully registered! " "Now login with your new credentials.")


@click.command(name="register", help="Register a new Registry account")
@click.option("--username", type=str, required=True, prompt=True)
@click.option("--email", type=str, required=True, prompt=True)
@click.option("--password", type=str, required=True, prompt=True, hide_input=True)
@click.option(
    "--confirm_password", type=str, required=True, prompt=True, hide_input=True
)
def register(username, email, password, confirm_password):
    """Register a new Registry account CLI command."""
    do_register(username, email, password, confirm_password)