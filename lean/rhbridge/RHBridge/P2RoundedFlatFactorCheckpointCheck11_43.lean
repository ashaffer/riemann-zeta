import RHBridge.P2RoundedFlatFactorCheckpointData11

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel11FlatComponentChunk43 :
    P2RoundedFactorCheckpointData.panel11FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel11TruncatedOddComponents).get ⟨19, by decide⟩ := by
  decide +kernel

theorem panel11FlatOdd19_eq :
    P2RoundedFactorCheckpointData.panel11FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel11TruncatedOddComponents).get ⟨19, by decide⟩ := by
  exact panel11FlatComponentChunk43

end RHP2Bridge
