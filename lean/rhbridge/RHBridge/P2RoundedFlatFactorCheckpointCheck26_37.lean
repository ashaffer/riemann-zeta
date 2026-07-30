import RHBridge.P2RoundedFlatFactorCheckpointData26

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel26FlatComponentChunk37 :
    P2RoundedFactorCheckpointData.panel26FlatOdd13 =
      (P2RoundedFactorCheckpointData.panel26TruncatedOddComponents).get ⟨13, by decide⟩ := by
  decide +kernel

theorem panel26FlatOdd13_eq :
    P2RoundedFactorCheckpointData.panel26FlatOdd13 =
      (P2RoundedFactorCheckpointData.panel26TruncatedOddComponents).get ⟨13, by decide⟩ := by
  exact panel26FlatComponentChunk37

end RHP2Bridge
