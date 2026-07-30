import RHBridge.P2RoundedFlatFactorCheckpointData18

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel18FlatComponentChunk43 :
    P2RoundedFactorCheckpointData.panel18FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel18TruncatedOddComponents).get ⟨19, by decide⟩ := by
  decide +kernel

theorem panel18FlatOdd19_eq :
    P2RoundedFactorCheckpointData.panel18FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel18TruncatedOddComponents).get ⟨19, by decide⟩ := by
  exact panel18FlatComponentChunk43

end RHP2Bridge
