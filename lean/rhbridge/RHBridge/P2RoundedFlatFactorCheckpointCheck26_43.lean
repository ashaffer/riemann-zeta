import RHBridge.P2RoundedFlatFactorCheckpointData26

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel26FlatComponentChunk43 :
    P2RoundedFactorCheckpointData.panel26FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel26TruncatedOddComponents).get ⟨19, by decide⟩ := by
  decide +kernel

theorem panel26FlatOdd19_eq :
    P2RoundedFactorCheckpointData.panel26FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel26TruncatedOddComponents).get ⟨19, by decide⟩ := by
  exact panel26FlatComponentChunk43

end RHP2Bridge
