import RHBridge.P2RoundedFlatFactorCheckpointData18

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel18FlatComponentChunk37 :
    P2RoundedFactorCheckpointData.panel18FlatOdd13 =
      (P2RoundedFactorCheckpointData.panel18TruncatedOddComponents).get ⟨13, by decide⟩ := by
  decide +kernel

theorem panel18FlatOdd13_eq :
    P2RoundedFactorCheckpointData.panel18FlatOdd13 =
      (P2RoundedFactorCheckpointData.panel18TruncatedOddComponents).get ⟨13, by decide⟩ := by
  exact panel18FlatComponentChunk37

end RHP2Bridge
