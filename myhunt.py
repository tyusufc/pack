import constInfo
import chat
import chr
import net
import time

last_attack_time = 0  # saldırı gecikmesi için zaman tutucu

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
    return constInfo.StartAutoHunt == 1

def UpdateAutoHunt():
    global last_attack_time

    if not constInfo.StartAutoHunt:
        return

    if not hasattr(constInfo, "AutoHunt_Attack") or constInfo.AutoHunt_Attack != 1:
        return

    now = time.clock()
    if now - last_attack_time < 1.0:
        return  # Her 1 saniyede 1 kez saldırı yapsın

    vid = GetNearestMonsterVid()
    if vid == 0:
        return  # Etrafta yaratık yoksa hiçbir şey yapma

    chr.SelectInstance(vid)
    net.SendAttackPacket(vid)
    chat.AppendChat(chat.CHAT_TYPE_INFO, "⚔️ Düşmana saldırıldı.")

    last_attack_time = now

def GetNearestMonsterVid():
    vid = -1
    minDistance = 999999
    for i in xrange(chr.GetInstanceCount()):
        instance = chr.GetInstanceByIndex(i)
        if chr.IsNPC(instance) and not chr.IsDead(instance):
            x, y, _ = chr.GetPixelPosition(instance)
            dist = chr.GetDistance(instance)
            if dist < minDistance:
                minDistance = dist
                vid = instance
    return vid
