
import constInfo
import chat

print("✅ myhunt.py yüklendi")

def StartAutoHunt():
    print("✅ StartAutoHunt() çalıştı")
    if not constInfo.StartAutoHunt:
        constInfo.StartAutoHunt = 1
        chat.AppendChat(chat.CHAT_TYPE_INFO, "✅ Otomatik Av Başladı.")

def StopAutoHunt():
    print("🛑 StopAutoHunt() çalıştı")
    if constInfo.StartAutoHunt:
        constInfo.StartAutoHunt = 0
        chat.AppendChat(chat.CHAT_TYPE_INFO, "❌ Otomatik Av Durduruldu.")

def IsRunning():
    print("🔁 IsRunning() çağrıldı")
    return constInfo.StartAutoHunt == 1

def UpdateAutoHunt():
    print("🔄 UpdateAutoHunt() çağrıldı")
    if constInfo.StartAutoHunt:
        # Placeholder for periodic update logic
        chat.AppendChat(chat.CHAT_TYPE_INFO, "🔄 Otomatik Av Güncelleme")
