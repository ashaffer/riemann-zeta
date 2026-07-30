import RHBridge.P2RoundedFlatFactorCheckpointData11

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel11FlatComponentChunk47 :
    P2RoundedFactorCheckpointData.panel11FlatOdd23 =
      (P2RoundedFactorCheckpointData.panel11TruncatedOddComponents).get ⟨23, by decide⟩ := by
  decide +kernel

theorem panel11FlatOdd23_eq :
    P2RoundedFactorCheckpointData.panel11FlatOdd23 =
      (P2RoundedFactorCheckpointData.panel11TruncatedOddComponents).get ⟨23, by decide⟩ := by
  exact panel11FlatComponentChunk47

end RHP2Bridge
