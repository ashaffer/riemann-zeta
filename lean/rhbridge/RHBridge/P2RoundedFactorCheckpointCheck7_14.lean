import RHBridge.P2RoundedFactorCheckpointData7

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel7FactorChunk14 :
    P2RoundedFactorCheckpointData.panel7Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨7, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel7Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨7, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel7Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨7, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel7Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨7, by decide⟩ := by
  decide +kernel

theorem panel7Prefix56_eq :
    P2RoundedFactorCheckpointData.panel7Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk14.1

theorem panel7Prefix57_eq :
    P2RoundedFactorCheckpointData.panel7Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk14.2.1

theorem panel7Prefix58_eq :
    P2RoundedFactorCheckpointData.panel7Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk14.2.2.1

theorem panel7Prefix59_eq :
    P2RoundedFactorCheckpointData.panel7Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk14.2.2.2

end RHP2Bridge
