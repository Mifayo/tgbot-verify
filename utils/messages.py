"""消息模板"""
from config import CHANNEL_URL, VERIFY_COST, HELP_NOTION_URL


def get_welcome_message(full_name: str, invited_by: bool = False) -> str:
    """获取欢迎消息"""
    msg = (
        f"🎉 Welcome, {full_name}!\n"
        "You have successfully registered and received 1 point.\n"
    )
    if invited_by:
        msg += "Thanks for joining via an invite link. The inviter has received 2 points.\n"

    msg += (
        "\nThis bot can automatically complete SheerID verifications.\n"
        "Quick Start:\n"
        "/about - Learn about bot features\n"
        "/balance - Check point balance\n"
        "/help - View full command list\n\n"
        "Get More Points:\n"
        "/qd - Daily check-in\n"
        "/invite - Invite friends\n"
        f"Join Channel: {CHANNEL_URL}"
    )
    return msg


def get_about_message() -> str:
    """获取关于消息"""
    return (
        "🤖 SheerID Auto-Verification Bot\n"
        "\n"
        "Features:\n"
        "- Automated SheerID Student/Teacher verification\n"
        "- Supports Gemini One Pro, ChatGPT Teacher K12, Spotify Student, YouTube Student, Bolt.new Teacher\n"
        "\n"
        "Earning Points:\n"
        "- Registration bonus: 1 point\n"
        "- Daily check-in: +1 point\n"
        "- Invite friends: +2 points/person\n"
        "- Redeem gift codes (as per code value)\n"
        f"- Join Channel: {CHANNEL_URL}\n"
        "\n"
        "How to Use:\n"
        "1. Start verification on the website and copy the full verification link\n"
        "2. Send /verify, /verify2, /verify3, /verify4, or /verify5 with the link\n"
        "3. Wait for processing and check the result\n"
        "4. Bolt.new verification automatically retrieves the code. To query manually, use /getV4Code <verification_id>\n"
        "\n"
        "For more commands, send /help"
    )


def get_help_message(is_admin: bool = False) -> str:
    """获取帮助消息"""
    msg = (
        "📖 SheerID Auto-Verification Bot - Help\n"
        "\n"
        "User Commands:\n"
        "/start - Start using (Register)\n"
        "/about - Learn about bot features\n"
        "/balance - Check point balance\n"
        "/qd - Daily check-in (+1 point)\n"
        "/invite - Generate invite link (+2 points/person)\n"
        "/use <code> - Redeem gift code for points\n"
        f"/verify <link> - Gemini One Pro Verification (-{VERIFY_COST} points)\n"
        f"/verify2 <link> - ChatGPT Teacher K12 Verification (-{VERIFY_COST} points)\n"
        f"/verify3 <link> - Spotify Student Verification (-{VERIFY_COST} points)\n"
        f"/verify4 <link> - Bolt.new Teacher Verification (-{VERIFY_COST} points)\n"
        f"/verify5 <link> - YouTube Student Premium Verification (-{VERIFY_COST} points)\n"
        "/getV4Code <verification_id> - Get Bolt.new verification code\n"
        "/help - View this help message\n"
        f"Verification Failure Help: {HELP_NOTION_URL}\n"
    )

    if is_admin:
        msg += (
            "\nAdmin Commands:\n"
            "/addbalance <User ID> <Points> - Add points to user\n"
            "/block <User ID> - Block user\n"
            "/white <User ID> - Unblock user\n"
            "/blacklist - View blacklist\n"
            "/genkey <code> <Points> [Times] [Days] - Generate gift code\n"
            "/listkeys - View gift code list\n"
            "/broadcast <Text> - Broadcast message to all users\n"
        )

    return msg


def get_insufficient_balance_message(current_balance: int) -> str:
    """获取积分不足消息"""
    return (
        f"Insufficient points! Need {VERIFY_COST} points, current balance {current_balance} points.\n\n"
        "How to get points:\n"
        "- Daily check-in /qd\n"
        "- Invite friends /invite\n"
        "- Redeem code /use <code>"
    )


def get_verify_usage_message(command: str, service_name: str) -> str:
    """获取验证命令使用说明"""
    return (
        f"Usage: {command} <SheerID Link>\n\n"
        "Example:\n"
        f"{command} https://services.sheerid.com/verify/xxx/?verificationId=xxx\n\n"
        "How to get the link:\n"
        f"1. Visit the {service_name} verification page\n"
        "2. Start the verification process\n"
        "3. Copy the full URL from the browser address bar\n"
        f"4. Submit using the {command} command"
    )
