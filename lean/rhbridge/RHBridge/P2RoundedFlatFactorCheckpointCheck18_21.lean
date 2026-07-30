import RHBridge.P2RoundedFlatFactorCheckpointData18

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel18FlatComponentChunk21 :
    P2RoundedFactorCheckpointData.panel18FlatEven21 =
      (P2RoundedFactorCheckpointData.panel18TruncatedEvenComponents).get ⟨21, by decide⟩ := by
  decide +kernel

theorem panel18FlatEven21_eq :
    P2RoundedFactorCheckpointData.panel18FlatEven21 =
      (P2RoundedFactorCheckpointData.panel18TruncatedEvenComponents).get ⟨21, by decide⟩ := by
  exact panel18FlatComponentChunk21

end RHP2Bridge
