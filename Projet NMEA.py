import folium

trame = "$GPGGA,174133.648,4806.570,N,00508.393,E,1,12,1.0,0.0,M,0.0,M,,*6B"

def TrameNMEA(trame):
    trameX=trame.rstrip().split(",")
    heureX= trameX[1]
    heure = heureX.rstrip().split(".")
    heure = heure[0]
    heure=(heure[0]+heure[1]+":"+heure[2]+heure[3]+":"+heure[4]+heure[5])
    cardinal_latitude= trameX[3]
    latitude_degreX = trameX[2]
    latitude_degre = latitude_degreX[0:2]
    latitude_secondesX =int(latitude_degreX[5:8])*10**-3*60
    latitude_secondesX=str(latitude_secondesX)
    latitude_minute=latitude_secondesX[0:2]
    latitude_seconde=latitude_secondesX[3:5]
    latitudeDD=float(trameX[2])*10**-2
    latitude_DMS=latitude_degre+"°"+latitude_minute+"'"+ latitude_seconde+"''"+cardinal_latitude
    cardinal_longitude= trameX[5]
    longitude_degreX= trameX[4]
    longitude_degre=longitude_degreX[2]
    longitude_secondeX=int(longitude_degreX[6:9])*10**-3*60
    longitude_secondeX=str(longitude_secondeX)
    longitude_minute=longitude_secondeX[0:2]
    longitude_seconde=longitude_secondeX[3:5]
    longitudeDD=float(trameX[4])*10**-2
    longitude_DMS=longitude_degre+"°"+longitude_minute+"'"+ longitude_seconde+"''"+cardinal_longitude
    altitude=trameX[9]+" m"
    nombre_satellite= trameX[7]
    print("Heure : ",heure," Latitude : ",latitude_DMS," Longitude : ",longitude_DMS," Altitude : ",altitude," Nombre de satellites : ",nombre_satellite)
    maCarte= folium.Map(location=[latitudeDD,longitudeDD],zoom_start=8)
    center=[latitudeDD,longitudeDD]
    folium.Marker(center).add_to(maCarte)
    folium.Circle(center,radius=100000,fill=True,color="red").add_to(maCarte)
    maCarte.save('Carte.html')
    print(latitudeDD,longitudeDD)
          
    

TrameNMEA(trame)

