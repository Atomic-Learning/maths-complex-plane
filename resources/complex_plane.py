#!/usr/bin/env python3
"""
Generate a complex plane (Argand diagram) showing complex numbers as points.
Outputs to complex-plane.png in the same directory.
"""

import matplotlib.pyplot as plt

# Create figure and axis
fig, ax = plt.subplots(1, 1, figsize=(9, 9), dpi=150)
ax.set_aspect('equal')
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
ax.axhline(y=0, color='k', linewidth=1.5)
ax.axvline(x=0, color='k', linewidth=1.5)

# Add axis labels
ax.set_xlabel('Real Part (Re)', fontsize=12, fontweight='bold')
ax.set_ylabel('Imaginary Part (Im)', fontsize=12, fontweight='bold')

# Define some example complex numbers
examples = [
    (3, 0, '3'),
    (0, 2, '2i'),
    (1, 1, '1 + i'),
    (2, 1.5, '2 + 1.5i'),
    (-1, 2, '-1 + 2i'),
    (-2, -1, '-2 - i'),
    (1.5, -2.5, '1.5 - 2.5i'),
]

# Plot example points
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#F7DC6F', '#BB8FCE']
for i, (real, imag, label) in enumerate(examples):
    ax.plot(real, imag, 'o', markersize=10, color=colors[i % len(colors)])
    # Draw line from origin to point
    ax.plot([0, real], [0, imag], '--', color=colors[i % len(colors)], alpha=0.4, linewidth=1.5)
    # Label the point
    offset_x = 0.3 if real >= 0 else -0.3
    offset_y = 0.3 if imag >= 0 else -0.3
    ax.text(real + offset_x, imag + offset_y, label, fontsize=10, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor=colors[i % len(colors)], alpha=0.3))

# Set ticks
ax.set_xticks([-4, -3, -2, -1, 0, 1, 2, 3, 4])
ax.set_yticks([-4, -3, -2, -1, 0, 1, 2, 3, 4])
ax.tick_params(labelsize=10)

# Add annotation for real and imaginary axes
ax.text(3.5, -0.2, 'Real axis', fontsize=10, style='italic', color='gray', ha='center')
ax.text(-0.2, 3.3, 'Imaginary axis', fontsize=10, style='italic', color='gray', rotation=90, va='center')

plt.tight_layout()
plt.savefig('complex-plane.png', dpi=150, bbox_inches='tight', facecolor='white')
print("Generated: complex-plane.png")
plt.close()
