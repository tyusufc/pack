import constInfo
import chat
import chr
import net
import time
import player
import networkModule



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
    networkModule.stream.SendAttackPacket(vid)
    chat.AppendChat(chat.CHAT_TYPE_INFO, "⚔️ Düşmana saldırıldı.")

    last_attack_time = now

def GetNearestMonsterVid():
    minDistance = 999999
    nearestVID = 0

    for vid in xrange(0, 65535):
        if not chr.HasInstance(vid):
            continue

        if not chr.IsNPC(vid):
            continue

        px, py, pz = player.GetMainCharacterPosition()
        x, y, z = chr.GetPixelPosition(vid)

        distance = ((x - px) ** 2 + (y - py) ** 2) ** 0.5

        if distance < minDistance:
            minDistance = distance
            nearestVID = vid

    return nearestVID