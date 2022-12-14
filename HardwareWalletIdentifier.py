import winreg

def main():
    access_registry = winreg.ConnectRegistry(None,winreg.HKEY_LOCAL_MACHINE)
    access_key = winreg.OpenKey(access_registry,r'SYSTEM\ControlSet001\Enum\USB')
    
    connected_devices = []
    wallet_devices = []
    print('+------------------------------------------------------------------------------+')
    print('|                          Hardware Wallet Identifier                          |')
    print('+------------------------------------------------------------------------------+')
    print('Previously connected devices:')
    print('--------------------------------------------------------------------------------')
    for n in range(1000):
        try:
            x = winreg.EnumKey(access_key,n)
            print(x)
            connected_devices.append(x)
            
        except:
            break
    print('')
    print('--------------------------------------------------------------------------------')
    print('The following Hardware Wallets may have been connected to this device: ')

    #BitBox
    if any('VID_03EB&PID_2402' in s for s in connected_devices):
        print(' - BitBox01 Hardware Wallet')
        wallet_devices.append('Bitbox_1')

    if any('VID_03EB&PID_2403' in s for s in connected_devices):
        print(' BitBox02 Hardware Wallet')
        wallet_devices.append('Bitbox_2')

    #JuBiter Blade
    if any('VID_096E&PID_0891' in s for s in connected_devices):
        print(' - JuBiter Blade Hardware Wallet')
        wallet_devices.append('JuBiter_Blade')
    #Optimum
    if any('VID_1209&PID_AAAA' in s for s in connected_devices):
        print(' - Optimum Hardware Wallet')
        wallet_devices.append('Optimum')

    #SafeWISE CoinSafe
    if any('VID_1209&PID_ABBA' in s for s in connected_devices):
        print(' - SafeWISE CoinSafe Hardware Wallet')
        wallet_devices.append('SafeWISE')

    #Trezor
    if 'VID_1209&PID_53C0' in connected_devices or 'VID_1209&PID_53C1' in connected_devices:
        print(' - Trezor Hardware Wallet')
        wallet_devices.append('Trezor_1')

    if any('VID_534C&PID_0001' in s for s in connected_devices):
        print(" - Trezor Hardware Wallet")
        wallet_devices.append('Trezor_2')

    #Monero 
    if 'VID_1209&PID_B0B0' in connected_devices or 'VID_1209&PID_C0DA' in connected_devices or 'VID1209&PID_D00D' in connected_devices:
        print(' - Monero Hardware Wallet')
        wallet_devices.append('Monero')

    #Secalot
    if 'VID_1209&PID_7000' in connected_devices or 'VID_1209&PID_7001' in connected_devices:
        print(' - Secalot Hardware Wallet')
        wallet_devices.append('Secalot')

    #OpenDime
    if any('VID_1209&PID_7551' in s for s in connected_devices):
        print(' - OpenDime Hardware Wallet')
        wallet_devices.append('OpenDime')

    #Opolo
    if 'VID_1209&PID_9998' in connected_devices or 'VID_1209&PID_9999' in connected_devices:
        print(' - Opolo Hardware Wallet')
        wallet_devices.append('Opolo')
    
    #BitLox
    if 'VID_2341&PID_003D' in connected_devices or 'VID_2341&PID_003E' in connected_devices:
        print(' - BitLox Hardware Wallet')
        wallet_devices.append('BitLox')

    #Ledger
    if 'VID_2581&PID_1807' in connected_devices or 'VID_2581&PID_1808' in connected_devices or 'VID_2581&PID_1B7C' in connected_devices or 'VID_258&PID_1B7C' in connected_devices or 'VID_2581&PID_2B7C' in connected_devices or 'VID_2581&PID_3B7C' in connected_devices or 'VID_2581&PID_4B7C' in connected_devices:
        print(' - Ledger HW1 hardware Wallet')
        wallet_devices.append('Ledger_1')

    if any('VID_2581&PID_F1D1' in s for s in connected_devices):
        print(' - Ledger HW1 or Nano S Plus Hardware Wallet')
        wallet_devices.append('Ledger_2')
    
    if any('VID_2C97' in s for s in connected_devices):
        print(' - Ledger HW2, Ledger X, Ledger Blue or Ledger Nano S')
        wallet_devices.append('Ledger 3')

    #KeepKey
    if any('VID_2B24' in s for s in connected_devices):
        print(' - KeepKey Hardware Wallet')
        wallet_devices.append('KeepKey')
    
    #D'CENT
    if any('VID_2F48&PID_2130' in s for s in connected_devices):
        print(" - D'CENT Hardware Wallet")
        wallet_devices.append("D'CENT")

    #CoinKite
    if any('VID_D13E&PID_CC10' in s for s in connected_devices):
        print(" - CoinKite Hardware Wallet")
        wallet_devices.append('CoinKite')
    
    if not wallet_devices:
        print("No Hardware Wallets have been identified!")
        print("")
    if wallet_devices:
        print("")

    print('--------------------------------------------------------------------------------')
    print('This list is not exhaustive! Please confirm your own findings!')
    print('https://github.com/INTERPOL-Innovation-Centre/HardwareWallets_DF_List')
    print('')
    input('Press any key to close.')

if __name__ == '__main__':
    main()