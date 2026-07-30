import RHBridge.P2RoundedFlatFactorCheckpointData31

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel31FlatComponentChunk4 :
    P2RoundedFactorCheckpointData.panel31FlatEven4 =
      (P2RoundedFactorCheckpointData.panel31TruncatedEvenComponents).get ⟨4, by decide⟩ := by
  decide +kernel

theorem panel31FlatEven4_eq :
    P2RoundedFactorCheckpointData.panel31FlatEven4 =
      (P2RoundedFactorCheckpointData.panel31TruncatedEvenComponents).get ⟨4, by decide⟩ := by
  exact panel31FlatComponentChunk4

end RHP2Bridge
