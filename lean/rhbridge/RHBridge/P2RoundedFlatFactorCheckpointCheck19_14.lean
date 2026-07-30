import RHBridge.P2RoundedFlatFactorCheckpointData19

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel19FlatComponentChunk14 :
    P2RoundedFactorCheckpointData.panel19FlatEven14 =
      (P2RoundedFactorCheckpointData.panel19TruncatedEvenComponents).get ⟨14, by decide⟩ := by
  decide +kernel

theorem panel19FlatEven14_eq :
    P2RoundedFactorCheckpointData.panel19FlatEven14 =
      (P2RoundedFactorCheckpointData.panel19TruncatedEvenComponents).get ⟨14, by decide⟩ := by
  exact panel19FlatComponentChunk14

end RHP2Bridge
