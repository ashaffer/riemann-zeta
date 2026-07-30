import RHBridge.P2RoundedFlatFactorCheckpointData19

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel19FlatComponentChunk1 :
    P2RoundedFactorCheckpointData.panel19FlatEven1 =
      (P2RoundedFactorCheckpointData.panel19TruncatedEvenComponents).get ⟨1, by decide⟩ := by
  decide +kernel

theorem panel19FlatEven1_eq :
    P2RoundedFactorCheckpointData.panel19FlatEven1 =
      (P2RoundedFactorCheckpointData.panel19TruncatedEvenComponents).get ⟨1, by decide⟩ := by
  exact panel19FlatComponentChunk1

end RHP2Bridge
