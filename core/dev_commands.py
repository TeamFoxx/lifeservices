# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
# »› Entwickelt von Foxx
# »› Copyright © 2024 Aurel Hoxha. Alle Rechte vorbehalten.
# »› GitHub: https://github.com/TeamFoxx
# »› Für Support und Anfragen kontaktieren Sie bitte hello@aurelhoxha.de
# »› Verwendung dieses Programms unterliegt den Bedingungen der MIT-Lizenz.
# »› Eine Kopie der Lizenz finden Sie in der Datei "LICENSE" im Hauptverzeichnis dieses Projekts.
# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
#
# ⏤ { imports } ⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤

from core import *

# ⏤ { pre-settings } ⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤

log = logging.getLogger(__name__)


class cog_reload(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.slash_command(
        name="reload_cog",
        description="Development | reloads a Cog",
        default_required_permissions=discord.Permissions(administrator=True),
        options=[
            Option(
                name="cog",
                description="The Cog to reload",
                option_type=str,
                autocomplete=True
            ),
            Option(
                name='sync-commands',
                description='Whether slash-commands should be updated; default False',
                option_type=bool,
                required=False
            )
        ],
        connector={'sync-commands': 'sync_slash_commands'},
        guild_ids=[907982168402325544]
    )
    @commands.is_owner()
    async def reload(self, ctx, cog: str, sync_slash_commands: bool = False):
        before = getattr(self.bot, 'sync_commands_on_cog_reload', False)
        self.bot.sync_commands_on_cog_reload = sync_slash_commands
        await ctx.defer(hidden=True)
        try:
            self.bot.reload_extension(f'cogs.{cog}')
            log.info(f"reloaded Cog \033[32m{cog}\033[0m")
            await ctx.respond(
                f"The Cog `{cog}` has been successful reloaded"
                f"{' and the slash-commands synced.' if sync_slash_commands is True else '.'}",
                hidden=True)
        except commands.ExtensionNotLoaded:
            await ctx.respond(f"There is no extension with the Name `{cog}` loaded", hidden=True)
        except Exception:
            with open("error.py", "w") as error:
                error.write(f"The following error occurred when trying to reload {cog}:\n\n")
                traceback.print_exc(file=error)
            await ctx.respond(file=discord.File(fp="error.py"))
            os.remove('error.py')
        self.sync_commands_on_cog_reload = before

    @reload.autocomplete_callback
    async def reload_cog_autocomplete(self, i, cog: str = None, sync_slash_commands: bool = False):
        if cog:
            await i.send_choices(
                [Choice(name, c.__init__.__globals__['__file__'].split('\\')[-1].replace('.py', '')) for name, c in
                 self.bot.cogs.items() if name.startswith(cog)])
        else:
            await i.send_choices(
                [Choice(name, c.__init__.__globals__['__file__'].split('\\')[-1].replace('.py', '')) for name, c in
                 self.bot.cogs.items()])

    print(f'Callback: {reload.autocomplete_func}')


def setup(coffee_bot):
    coffee_bot.add_cog(cog_reload(coffee_bot))
