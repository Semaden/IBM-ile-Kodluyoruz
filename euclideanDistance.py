import math

# Noktaların tanımlanması
points = [(1, 2), (4, 6), (5, 8), (9, 10), (12, 14)]

# Öklid mesafesi fonksiyonunun tanımlanması
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Mesafelerin hesaplanması ve saklanması
distances = []
for i in range(len(points)):
    for j in range(i+1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafenin bulunması ve yazdırılması
min_distance = min(distances)
print(f"Minimum mesafe: {min_distance}")
