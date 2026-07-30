import RHBridge.P2RoundedFlatFactorCheckpointData11

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel11FlatComponentChunk39 :
    P2RoundedFactorCheckpointData.panel11FlatOdd15 =
      (P2RoundedFactorCheckpointData.panel11TruncatedOddComponents).get ⟨15, by decide⟩ := by
  decide +kernel

theorem panel11FlatOdd15_eq :
    P2RoundedFactorCheckpointData.panel11FlatOdd15 =
      (P2RoundedFactorCheckpointData.panel11TruncatedOddComponents).get ⟨15, by decide⟩ := by
  exact panel11FlatComponentChunk39

end RHP2Bridge
