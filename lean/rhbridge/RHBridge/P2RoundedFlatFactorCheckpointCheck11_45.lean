import RHBridge.P2RoundedFlatFactorCheckpointData11

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel11FlatComponentChunk45 :
    P2RoundedFactorCheckpointData.panel11FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel11TruncatedOddComponents).get ⟨21, by decide⟩ := by
  decide +kernel

theorem panel11FlatOdd21_eq :
    P2RoundedFactorCheckpointData.panel11FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel11TruncatedOddComponents).get ⟨21, by decide⟩ := by
  exact panel11FlatComponentChunk45

end RHP2Bridge
