from __future__ import annotations

import argparse
import getpass
import sys

from app import STORE


def read_password(confirm: bool = True) -> str:
    password = getpass.getpass("密码: ")
    if confirm and password != getpass.getpass("再次输入密码: "):
        raise ValueError("两次输入的密码不一致")
    return password


def main() -> None:
    parser = argparse.ArgumentParser(description="几何围猎账号管理")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="创建账号")
    add_parser.add_argument("username")
    add_parser.add_argument("--role", choices=("admin", "player"), default="player")

    reset_parser = subparsers.add_parser("reset", help="重置密码")
    reset_parser.add_argument("username")

    status_parser = subparsers.add_parser("status", help="启用或禁用账号")
    status_parser.add_argument("username")
    status_parser.add_argument("state", choices=("enable", "disable"))

    subparsers.add_parser("list", help="列出账号")
    args = parser.parse_args()

    try:
        if args.command == "add":
            STORE.create_user(args.username, read_password(), args.role)
            print(f"已创建账号: {args.username} ({args.role})")
        elif args.command == "reset":
            STORE.update_user(args.username, password=read_password())
            print(f"已重置密码: {args.username}")
        elif args.command == "status":
            STORE.update_user(args.username, enabled=args.state == "enable")
            print(f"已{('启用' if args.state == 'enable' else '禁用')}账号: {args.username}")
        elif args.command == "list":
            for user in STORE.list_users():
                state = "启用" if user["enabled"] else "禁用"
                print(
                    f"{user['username']}\t{user['role']}\t{state}\t"
                    f"局数={user['runs']}\t最高分={user['best_score']}"
                )
    except ValueError as exc:
        print(f"错误: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc


if __name__ == "__main__":
    main()
