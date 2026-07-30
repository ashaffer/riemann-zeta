import RHBridge.P2RoundedFlatFactorCheckpointData19

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel19FlatComponentChunk28 :
    P2RoundedFactorCheckpointData.panel19FlatOdd4 =
      (P2RoundedFactorCheckpointData.panel19TruncatedOddComponents).get ⟨4, by decide⟩ := by
  decide +kernel

theorem panel19FlatOdd4_eq :
    P2RoundedFactorCheckpointData.panel19FlatOdd4 =
      (P2RoundedFactorCheckpointData.panel19TruncatedOddComponents).get ⟨4, by decide⟩ := by
  exact panel19FlatComponentChunk28

end RHP2Bridge
