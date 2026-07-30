import RHBridge.P2RoundedFactorCheckpointData25

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel25FactorChunk14 :
    P2RoundedFactorCheckpointData.panel25Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨25, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel25Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨25, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel25Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨25, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel25Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨25, by decide⟩ := by
  decide +kernel

theorem panel25Prefix56_eq :
    P2RoundedFactorCheckpointData.panel25Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk14.1

theorem panel25Prefix57_eq :
    P2RoundedFactorCheckpointData.panel25Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk14.2.1

theorem panel25Prefix58_eq :
    P2RoundedFactorCheckpointData.panel25Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk14.2.2.1

theorem panel25Prefix59_eq :
    P2RoundedFactorCheckpointData.panel25Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk14.2.2.2

end RHP2Bridge
