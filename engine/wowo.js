// Rig Wowo. Canvas 2D, forward kinematics.
// Sudut sendi: 0 = lurus ke bawah, 90 = horizontal ke depan, 180 = lurus ke atas.
// Dua varian: 'kaus' (kulit sawo + kaus merah WOWO, v3) dan 'stick' (stickman murni + topi merah, v4 - dipakai channel).
(function (g) {
  const C = {
    SKIN: '#C98B5A', HAIR: '#111111', RED: '#E63946', RED_DARK: '#B82A36', WHITE: '#FFFFFF',
    SANDAL: '#333333', DARK: '#1F1A17', MOUTH: '#7A1F2B', CREAM: '#F5F1E8', LINE: '#111111',
  };
  const rad = (d) => (d * Math.PI) / 180;
  const LEG = 44, TORSO = 72, HEAD = 27, ARM1 = 38, ARM2 = 36;

  function seg(ctx, x, y, a, l, w, col) {
    const nx = x + l * Math.sin(rad(a)), ny = y + l * Math.cos(rad(a));
    ctx.strokeStyle = col; ctx.lineWidth = w; ctx.lineCap = 'round';
    ctx.beginPath(); ctx.moveTo(x, y); ctx.lineTo(nx, ny); ctx.stroke();
    return [nx, ny];
  }
  function limb(ctx, x, y, a1, l1, a2, l2, w, col) {
    const j = seg(ctx, x, y, a1, l1, w, col);
    return seg(ctx, j[0], j[1], a2, l2, w, col);
  }
  function leg(ctx, a1, a2, stick) {
    const e = limb(ctx, 0, 0, a1, LEG, a2, LEG, stick ? 7 : 10, stick ? C.LINE : C.SKIN);
    ctx.fillStyle = stick ? C.LINE : C.SANDAL;
    ctx.beginPath(); ctx.ellipse(e[0] + 5, e[1] + 3, stick ? 9 : 12, stick ? 3.5 : 4.5, 0, 0, Math.PI * 2); ctx.fill();
  }
  function arm(ctx, sx, sy, a1, a2, stick) {
    if (stick) {
      const e = limb(ctx, sx, sy, a1, ARM1, a2, ARM2, 7, C.LINE);
      ctx.fillStyle = C.LINE; ctx.beginPath(); ctx.arc(e[0], e[1], 4.5, 0, Math.PI * 2); ctx.fill();
      return;
    }
    const e = limb(ctx, sx, sy, a1, ARM1, a2, ARM2, 9, C.SKIN);
    ctx.fillStyle = C.SKIN; ctx.beginPath(); ctx.arc(e[0], e[1], 5.5, 0, Math.PI * 2); ctx.fill();
    seg(ctx, sx, sy, a1, 15, 13, C.RED);
  }
  function face(ctx, f, ey) {
    const look = (f.look || 0) * 3, mode = f.mode || 'smile', open = f.mouth || 0;
    if (mode === 'wow') {
      for (const ex of [-9, 9]) {
        ctx.fillStyle = C.WHITE; ctx.strokeStyle = C.DARK; ctx.lineWidth = 2;
        ctx.beginPath(); ctx.arc(ex, ey, 6.5, 0, Math.PI * 2); ctx.fill(); ctx.stroke();
        ctx.fillStyle = C.DARK; ctx.beginPath(); ctx.arc(ex + look, ey, 2.6, 0, Math.PI * 2); ctx.fill();
      }
      ctx.fillStyle = C.MOUTH; ctx.beginPath(); ctx.ellipse(0, ey + 14, 5, 7, 0, 0, Math.PI * 2); ctx.fill();
      return;
    }
    if (f.blink) {
      ctx.strokeStyle = C.DARK; ctx.lineWidth = 2.6; ctx.lineCap = 'round';
      for (const ex of [-9, 9]) { ctx.beginPath(); ctx.moveTo(ex - 4, ey); ctx.lineTo(ex + 4, ey); ctx.stroke(); }
    } else {
      ctx.fillStyle = C.DARK;
      for (const ex of [-9, 9]) { ctx.beginPath(); ctx.arc(ex + look, ey, 3.2, 0, Math.PI * 2); ctx.fill(); }
    }
    if (mode === 'talk' && open > 0.05) {
      ctx.fillStyle = C.MOUTH; ctx.beginPath();
      ctx.ellipse(0, ey + 12, 5 + open * 2.5, 1.5 + open * 6, 0, 0, Math.PI * 2); ctx.fill();
    } else {
      ctx.strokeStyle = C.DARK; ctx.lineWidth = 2.6; ctx.lineCap = 'round';
      ctx.beginPath(); ctx.moveTo(-7, ey + 10); ctx.quadraticCurveTo(0, ey + 16, 7, ey + 10); ctx.stroke();
    }
  }
  function head(ctx, f, stick) {
    if (stick) {
      ctx.fillStyle = C.CREAM; ctx.strokeStyle = C.LINE; ctx.lineWidth = 3.5;
      ctx.beginPath(); ctx.arc(0, 0, HEAD, 0, Math.PI * 2); ctx.fill(); ctx.stroke();
      face(ctx, f, 9);
      // topi merah ala baseball, brim pendek ke depan (kanan)
      ctx.fillStyle = C.RED; ctx.strokeStyle = C.LINE; ctx.lineWidth = 3;
      ctx.beginPath(); ctx.moveTo(-HEAD + 1, -5); ctx.arc(0, -5, HEAD - 1, Math.PI, 0); ctx.lineTo(HEAD - 1, -5); ctx.closePath(); ctx.fill(); ctx.stroke();
      ctx.fillStyle = C.RED_DARK;
      ctx.beginPath(); ctx.roundRect(8, -12, 36, 9, 4.5); ctx.fill(); ctx.stroke();
      return;
    }
    ctx.fillStyle = C.SKIN;
    ctx.beginPath(); ctx.arc(0, 0, HEAD, 0, Math.PI * 2); ctx.fill();
    ctx.save(); ctx.scale(0.75, 0.75);
    ctx.fillStyle = C.HAIR; ctx.beginPath();
    ctx.moveTo(-36, -2); ctx.quadraticCurveTo(-40, -42, 0, -46); ctx.quadraticCurveTo(40, -42, 36, -2);
    ctx.quadraticCurveTo(32, -18, 26, -24); ctx.lineTo(18, -14); ctx.lineTo(10, -26); ctx.lineTo(0, -14);
    ctx.lineTo(-10, -26); ctx.lineTo(-18, -14); ctx.lineTo(-26, -24); ctx.quadraticCurveTo(-32, -16, -36, -2);
    ctx.closePath(); ctx.fill(); ctx.restore();
    face(ctx, f, 3);
  }

  // p: {variant, x, groundY, k, lean, bob, legF, legB, armF, armB, face:{mode,mouth,look,blink}}
  function drawWowo(ctx, p) {
    const stick = p.variant === 'stick';
    const k = p.k || 1.5;
    const hipX = p.x, hipY = p.groundY - LEG * 2 * 0.97 * k - (p.bob || 0);
    ctx.save();
    ctx.translate(hipX, hipY); ctx.scale(k, k);
    leg(ctx, p.legB[0], p.legB[1], stick);
    leg(ctx, p.legF[0], p.legF[1], stick);
    if (!stick) { ctx.fillStyle = C.WHITE; ctx.beginPath(); ctx.roundRect(-23, -6, 46, 26, 7); ctx.fill(); }
    ctx.save();
    ctx.rotate(rad(p.lean || 0)); // positif = condong ke depan
    const sx = 0, sy = stick ? -TORSO + 8 : -TORSO + 12;
    arm(ctx, sx, sy, p.armB[0], p.armB[1], stick);
    if (stick) {
      seg(ctx, 0, 0, 0, 0, 7, C.LINE);
      ctx.strokeStyle = C.LINE; ctx.lineWidth = 7; ctx.lineCap = 'round';
      ctx.beginPath(); ctx.moveTo(0, 0); ctx.lineTo(0, -TORSO); ctx.stroke();
    } else {
      ctx.fillStyle = C.RED; ctx.beginPath(); ctx.roundRect(-23, -TORSO, 46, TORSO - 2, 10); ctx.fill();
      ctx.fillStyle = C.WHITE; ctx.font = '800 12px Poppins, Arial, sans-serif';
      ctx.textAlign = 'center'; ctx.textBaseline = 'middle'; ctx.fillText('WOWO', 0, -TORSO + 36);
    }
    ctx.save(); ctx.translate(0, -TORSO - HEAD + 6); head(ctx, p.face || {}, stick); ctx.restore();
    arm(ctx, sx, sy, p.armF[0], p.armF[1], stick);
    ctx.restore();
    ctx.restore();
  }

  g.WOWO = { drawWowo, head, C, rad };
})(typeof window !== 'undefined' ? window : globalThis);
