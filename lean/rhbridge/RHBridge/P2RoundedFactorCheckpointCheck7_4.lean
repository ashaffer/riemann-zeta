import RHBridge.P2RoundedFactorCheckpointData7

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel7FactorChunk4 :
    P2RoundedFactorCheckpointData.panel7Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨7, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel7Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨7, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel7Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨7, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel7Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨7, by decide⟩ := by
  decide +kernel

theorem panel7Prefix16_eq :
    P2RoundedFactorCheckpointData.panel7Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk4.1

theorem panel7Prefix17_eq :
    P2RoundedFactorCheckpointData.panel7Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk4.2.1

theorem panel7Prefix18_eq :
    P2RoundedFactorCheckpointData.panel7Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk4.2.2.1

theorem panel7Prefix19_eq :
    P2RoundedFactorCheckpointData.panel7Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk4.2.2.2

end RHP2Bridge
