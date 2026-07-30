import RHBridge.P2RoundedFlatFactorCheckpointData19

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel19FlatComponentChunk31 :
    P2RoundedFactorCheckpointData.panel19FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel19TruncatedOddComponents).get ⟨7, by decide⟩ := by
  decide +kernel

theorem panel19FlatOdd7_eq :
    P2RoundedFactorCheckpointData.panel19FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel19TruncatedOddComponents).get ⟨7, by decide⟩ := by
  exact panel19FlatComponentChunk31

end RHP2Bridge
