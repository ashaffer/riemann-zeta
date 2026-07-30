import RHBridge.P2RoundedFactorCheckpointData25

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel25FactorChunk4 :
    P2RoundedFactorCheckpointData.panel25Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨25, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel25Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨25, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel25Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨25, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel25Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨25, by decide⟩ := by
  decide +kernel

theorem panel25Prefix16_eq :
    P2RoundedFactorCheckpointData.panel25Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk4.1

theorem panel25Prefix17_eq :
    P2RoundedFactorCheckpointData.panel25Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk4.2.1

theorem panel25Prefix18_eq :
    P2RoundedFactorCheckpointData.panel25Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk4.2.2.1

theorem panel25Prefix19_eq :
    P2RoundedFactorCheckpointData.panel25Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk4.2.2.2

end RHP2Bridge
