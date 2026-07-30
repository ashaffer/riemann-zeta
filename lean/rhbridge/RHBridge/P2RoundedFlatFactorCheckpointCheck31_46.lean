import RHBridge.P2RoundedFlatFactorCheckpointData31

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel31FlatComponentChunk46 :
    P2RoundedFactorCheckpointData.panel31FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel31TruncatedOddComponents).get ⟨22, by decide⟩ := by
  decide +kernel

theorem panel31FlatOdd22_eq :
    P2RoundedFactorCheckpointData.panel31FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel31TruncatedOddComponents).get ⟨22, by decide⟩ := by
  exact panel31FlatComponentChunk46

end RHP2Bridge
