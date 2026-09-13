"""
🛠️ TOOL DEFINITIONS & EXECUTION BACKEND
Mã nguồn chứa danh sách Tool Schemas (JSON Schema) và Execution Layer phục vụ cho MCP Server.
"""

import json
from typing import Dict, Any

# ==============================================================================
# 1. KHAI BÁO TOOL SCHEMAS CHUẨN NATIVE JSON SCHEMA (TASK 1.2)
# ==============================================================================

TOOLS_SCHEMA = [
    # Tool 1: Lấy dữ liệu tin nhắn từ discord
    {
        "name": "fetch_discord_messages",
        "description": "Lấy lịch sử tin nhắn từ một kênh (channel) cụ thể trong server Discord.",
        "parameters": {
            "type": "object",
            "properties": {
                "channel_name": {
                    "type": "string",
                    "description": "Tên kênh Discord cần lấy tin nhắn (ví dụ: 'thong-bao-lop-hoc', 'hoidap')"
                },
                "limit": {
                    "type": "integer",
                    "description": "Số lượng tin nhắn mới nhất cần lấy. Mặc định là 10 nếu không chỉ định."
                }
            },
            "required": ["channel_name"]
        }
    },
    
    # --------------------------------------------------------------------------
    # TODO 1.2: HỌC VIÊN HOÀN THIỆN TOOL SCHEMA CHO 'schedule_appointment'
    # 🎯 YÊU CẦU THIẾT KẾ SCHEMA (JSON SCHEMA STANDARD):
    # 1. Tool dùng để đặt lịch hẹn tư vấn học vụ với Cố vấn học tập VinUni.
    # 2. Thiết kế các tham số (properties) để LLM trích xuất:
    #    - student_id (string): Mã sinh viên cần đặt lịch (ví dụ: 'SV2026001')
    #    - datetime_str (string): Thời gian hẹn (ví dụ: '14:00 15/09/2026')
    #    - advisor_name (string): Tên cố vấn học tập
    # 3. Khai báo danh sách các trường bắt buộc (required).
    # --------------------------------------------------------------------------
    
    # Tool 2: Lưu nội dung ghi chú thành một file
    {
        "name": "save_summary_note",
        "description": "Lưu lại nội dung đã tổng hợp, ghi chú thành một file.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_name": {
                    "type": "string",
                    "description": "Tên file để lưu (ví dụ: 'tong_hop_hoidap.txt')"
                },
                "content": {
                    "type": "string",
                    "description": "Nội dung chi tiết cần được ghi chú lại."
                }
            },
            "required": ["file_name", "content"]
        }
    }
]

# ==============================================================================
# 2. MÔ PHỎNG DỮ LIỆU & HÀM THỰC THI TOOL (EXECUTION LAYER)
# ==============================================================================

# Cơ sở dữ liệu giả lập (Mock Database) cho Discord
MOCK_DISCORD_MESSAGES = {
    "thong-bao-lop-hoc": [
        {"author": "Admin", "content": "Ngày mai lớp học qua Zoom lúc 8h sáng nhé.", "timestamp": "2026-09-13T08:00:00Z"},
        {"author": "Labcoachs", "content": "Các bạn nhớ nộp bài tập Day 03 trước 23:59 hôm nay.", "timestamp": "2026-09-13T09:30:00Z"}
    ],
    "hoidap": [
        {"author": "SV01", "content": "Cho em hỏi tool schema là gì ạ?", "timestamp": "2026-09-13T10:00:00Z"},
        {"author": "Labcoachs", "content": "Là một định dạng JSON mô tả công cụ cho LLM hiểu em nhé.", "timestamp": "2026-09-13T10:15:00Z"}
    ]
}


def execute_fetch_discord_messages(channel_name: str, limit: int = 10) -> str:
    """Thực thi giả lập: Lấy tin nhắn từ Discord"""
    channel = channel_name.strip().replace("#", "")
    messages = MOCK_DISCORD_MESSAGES.get(channel)
    
    if messages:
        return json.dumps({
            "status": "SUCCESS",
            "channel": channel,
            "data": messages[-limit:] # Chỉ lấy số lượng tin nhắn theo limit
        }, ensure_ascii=False)
    else:
        return json.dumps({
            "status": "CHANNEL_NOT_FOUND",
            "message": f"Không tìm thấy kênh Discord nào có tên là '{channel}'"
        }, ensure_ascii=False)


def execute_save_summary_note(file_name: str, content: str) -> str:
    """Thực thi giả lập: Lưu nội dung tổng hợp ra file"""
    import os
    # Giả lập ghi file vào thư mục docs/ 
    # (Trong bài Lab thực tế, bạn có thể in ra terminal là được)
    try:
        save_path = os.path.join("docs", file_name)
        with open(save_path, "w", encoding="utf-8") as f:
            f.write(content)
        
        return json.dumps({
            "status": "SUCCESS",
            "file_name": file_name,
            "message": f"Đã lưu thành công nội dung ghi chú vào file '{file_name}'."
        }, ensure_ascii=False)
    except Exception as e:
        return json.dumps({
            "status": "ERROR",
            "message": f"Lỗi khi ghi file: {str(e)}"
        }, ensure_ascii=False)


# Router gọi tool thực tế
TOOL_ROUTER = {
    "fetch_discord_messages": execute_fetch_discord_messages,
    "save_summary_note": execute_save_summary_note
}

def dispatch_tool_call(tool_name: str, arguments: Dict[str, Any]) -> str:
    """Hàm trung chuyển thực thi tool"""
    if tool_name in TOOL_ROUTER:
        try:
            return TOOL_ROUTER[tool_name](**arguments)
        except Exception as e:
            return json.dumps({"status": "EXECUTION_ERROR", "error": str(e)}, ensure_ascii=False)
    return json.dumps({"status": "UNKNOWN_TOOL", "error": f"Tool '{tool_name}' không tồn tại!"}, ensure_ascii=False)
