import RHBridge.P2RoundedFlatFactorCheckpointData31

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel31FlatComponentChunk22 :
    P2RoundedFactorCheckpointData.panel31FlatEven22 =
      (P2RoundedFactorCheckpointData.panel31TruncatedEvenComponents).get ⟨22, by decide⟩ := by
  decide +kernel

theorem panel31FlatEven22_eq :
    P2RoundedFactorCheckpointData.panel31FlatEven22 =
      (P2RoundedFactorCheckpointData.panel31TruncatedEvenComponents).get ⟨22, by decide⟩ := by
  exact panel31FlatComponentChunk22

end RHP2Bridge
