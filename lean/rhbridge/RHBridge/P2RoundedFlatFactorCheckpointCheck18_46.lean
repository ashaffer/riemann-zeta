import RHBridge.P2RoundedFlatFactorCheckpointData18

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel18FlatComponentChunk46 :
    P2RoundedFactorCheckpointData.panel18FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel18TruncatedOddComponents).get ⟨22, by decide⟩ := by
  decide +kernel

theorem panel18FlatOdd22_eq :
    P2RoundedFactorCheckpointData.panel18FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel18TruncatedOddComponents).get ⟨22, by decide⟩ := by
  exact panel18FlatComponentChunk46

end RHP2Bridge
