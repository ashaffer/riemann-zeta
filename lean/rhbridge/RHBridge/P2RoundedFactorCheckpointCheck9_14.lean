import RHBridge.P2RoundedFactorCheckpointData9

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel9FactorChunk14 :
    P2RoundedFactorCheckpointData.panel9Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨9, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel9Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨9, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel9Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨9, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel9Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨9, by decide⟩ := by
  decide +kernel

theorem panel9Prefix56_eq :
    P2RoundedFactorCheckpointData.panel9Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk14.1

theorem panel9Prefix57_eq :
    P2RoundedFactorCheckpointData.panel9Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk14.2.1

theorem panel9Prefix58_eq :
    P2RoundedFactorCheckpointData.panel9Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk14.2.2.1

theorem panel9Prefix59_eq :
    P2RoundedFactorCheckpointData.panel9Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk14.2.2.2

end RHP2Bridge
