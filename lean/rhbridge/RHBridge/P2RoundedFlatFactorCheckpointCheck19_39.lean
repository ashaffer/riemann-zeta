import RHBridge.P2RoundedFlatFactorCheckpointData19

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel19FlatComponentChunk39 :
    P2RoundedFactorCheckpointData.panel19FlatOdd15 =
      (P2RoundedFactorCheckpointData.panel19TruncatedOddComponents).get ⟨15, by decide⟩ := by
  decide +kernel

theorem panel19FlatOdd15_eq :
    P2RoundedFactorCheckpointData.panel19FlatOdd15 =
      (P2RoundedFactorCheckpointData.panel19TruncatedOddComponents).get ⟨15, by decide⟩ := by
  exact panel19FlatComponentChunk39

end RHP2Bridge
