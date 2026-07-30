import RHBridge.P2RoundedFactorCheckpointData18

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel18FactorChunk14 :
    P2RoundedFactorCheckpointData.panel18Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨18, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel18Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨18, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel18Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨18, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel18Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨18, by decide⟩ := by
  decide +kernel

theorem panel18Prefix56_eq :
    P2RoundedFactorCheckpointData.panel18Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk14.1

theorem panel18Prefix57_eq :
    P2RoundedFactorCheckpointData.panel18Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk14.2.1

theorem panel18Prefix58_eq :
    P2RoundedFactorCheckpointData.panel18Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk14.2.2.1

theorem panel18Prefix59_eq :
    P2RoundedFactorCheckpointData.panel18Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk14.2.2.2

end RHP2Bridge
